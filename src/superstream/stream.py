from functools import reduce
from typing import TypeVar, Callable, List, Set, Generic, Dict, Iterable, Optional, Any
from itertools import islice, chain, count, starmap, takewhile, dropwhile
from collections import deque

T = TypeVar('T')
R = TypeVar('R')
K = TypeVar('K')
U = TypeVar('U')

_initial_missing = object()

def side_effect(func, iterable):
    for item in iterable:
        func(item)
        yield item

class Stream(Generic[T]):
    def __init__(self, stream: Iterable[T]):
        self._stream = iter(stream)

    def __iter__(self):
        return self._stream

    @staticmethod
    def of(*args: T) -> 'Stream[T]':
        return Stream(args)

    def map(self, func: Callable[[T], R]) -> 'Stream[R]':
        return Stream(map(func, self._stream))

    def star_map(self, func: Callable[..., R]) -> 'Stream[R]':
        return Stream(starmap(func, self._stream))

    def flat_map(self, func: Callable[[T], 'Stream[R]']) -> 'Stream[R]':
        return Stream(chain.from_iterable(map(func, self._stream)))

    def filter(self, func: Callable[[T], bool]) -> 'Stream[T]':
        return Stream(filter(func, self._stream))

    def for_each(self, func: Callable[[T], None]) -> None:
        deque(map(func, self._stream), maxlen=0)

    def peek(self, func: Callable[[T], None]) -> 'Stream[T]':
        if func is None:
            return self
        return Stream(side_effect(func, self._stream))

    def distinct(self):
        return Stream(list(dict.fromkeys(self._stream)))

    def sorted(self, key=None, reverse=False) -> 'Stream[T]':
        return Stream(sorted(self._stream, key=key, reverse=reverse))

    def count(self) -> int:
        cnt = count()
        deque(zip(self._stream, cnt), maxlen=0)
        return next(cnt)

    def sum(self, start: T = 0) -> T:
        return sum(self._stream, start)

    def group_by(self, classifier: Callable[[T], K]) -> Dict[K, List[T]]:
        groups = {}
        for i in self._stream:
            groups.setdefault(classifier(i), []).append(i)
        return groups

    def reduce(self, func: Callable[[T, T], T], initial: T = _initial_missing) -> Optional[T]:
        if initial is not _initial_missing:
            return reduce(func, self._stream, initial)
        else:
            try:
                return reduce(func, self._stream)
            except TypeError as e:
                if "reduce() of empty" in e.args[0]:
                    return None
                else:
                    raise

    def limit(self, max_size: int) -> 'Stream[T]':
        return Stream(islice(self._stream, max_size))

    def skip(self, n: int) -> 'Stream[T]':
        return Stream(islice(self._stream, n, None))

    def take_while(self, pred: Callable[[T], bool]) -> 'Stream[T]':
        return Stream(takewhile(pred, self._stream))

    def drop_while(self, pred: Callable[[T], bool]) -> 'Stream[T]':
        return Stream(dropwhile(pred, self._stream))

    def min(self, key: Callable[[T], Any] = None, default: T = None) -> Optional[T]:
        """
        :param default: use default value when stream is empty
        :param key: at lease supported __lt__ method
        """
        if key is not None:
            return min(self._stream, key=key, default=default)
        return min(self._stream, default=default)

    def max(self, key: Callable[[T], Any] = None, default: T = None) -> Optional[T]:
        """
        :param default: use default value when stream is empty
        :param key: at lease supported __lt__ method
        """
        if key is not None:
            return max(self._stream, key=key, default=default)
        return max(self._stream, default=default)

    def find_first(self) -> Optional[T]:
        return next(self._stream, None)

    def any_match(self, func: Callable[[T], bool]) -> bool:
        """
        this is equivalent to
            for i in self._stream:
                if func(i):
                    return True
            return False
        :param func:
        :return:
        """
        return any(map(func, self._stream))

    def all_match(self, func: Callable[[T], bool]) -> bool:
        return all(map(func, self._stream))

    def none_match(self, func: Callable[[T], bool]) -> bool:
        return not self.any_match(func)

    def to_list(self) -> List[T]:
        return list(self._stream)

    def to_set(self) -> Set[T]:
        return set(self._stream)

    def to_dict(self, k: Callable[[T], K], v: Callable[[T], U]) -> Dict[K, U]:
        return {k(i): v(i) for i in self._stream}

    def to_map(self, k: Callable[[T], K], v: Callable[[T], U]) -> Dict[K, U]:
        return self.to_dict(k, v)

    def collect(self, func: Callable[[Iterable[T]], R]) -> R:
        return func(self._stream)

    def collects(self, func: Callable[[Iterable[T]], Iterable[R]]) -> 'Stream[R]':
        return Stream(func(self._stream))
