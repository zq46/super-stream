# SuperStream

[![Test](https://github.com/Shimada666/super-stream/actions/workflows/main.yml/badge.svg)](https://github.com/Shimada666/super-stream/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/Shimada666/python-stream/branch/master/graph/badge.svg)](https://codecov.io/gh/Shimada666/super-stream)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)
[![image](https://img.shields.io/pypi/v/superstream.svg?style=flat)](https://pypi.python.org/pypi/superstream)

在用使用过 Typescript 与 Java 方便的链式调用后，回到 Python 再想实现同样的功能
高阶函数的套娃让你很痛苦吧？
性能开销都在其次，主要是写着蛋疼啊！

现在一个轻量级流式处理工具来了，利用 python 内置特性，他可以轻松实现

* 更高的可读性
* 惰性求值（无论中途map，filter多少次，数据只在最后遍历一次）
* 完善的类型提示，即使你使用 lambda

## 安装

```shell
pip install superstream
```

## 使用
[查看文档](https://shimada666.github.io/super-stream/) 

### 与 java stream 的对照

* 暂不支持并行 parallel
* 大部分功能已支持，行为相同

### 主要方法支持列表

- [X]  map
- [X]  forEach
- [X]  filter
- [X]  reduce
- [X]  sorted
- [X]  limit
- [X]  skip
- [X]  count
- [X]  min/max
- [X]  distinct
- [X]  flatMap
- [X]  findAny/findFirst
- [X]  anyMatch/allMatch/noneMatch
- [X]  of
- [X]  collect(toList/toSet/toMap/groupingBy)


| Java Stream         | Python Stream | 备注                                                                                     |
| ------------------- | ------------- | ---------------------------------------------------------------------------------------- |
| filter              | filter        |                                                                                          |
| map                 | map           |                                                                                          |
| -                   | star_map      | map 的 \* 参数解包版本                                                                   |
| flatMap             | flat_map      |                                                                                          |
| collect             | collect       |                                                                                          |
| -                   | collects      | collect 对应的中间操作，collects(collector) 相当于 Java 中的 collect(collector).stream() |
| collect(groupingBy) | group_by      |                                                                                          |
| collect(toList)     | to_list       |                                                                                          |
| collect(toSet)      | to_set        |                                                                                          |
| collect(toMap)      | to_dict       |                                                                                          |
| collect(toMap)      | to_map        | to_dict 的别名，保持与 Java 的一致                                                       |
| distinct            | distinct      |                                                                                          |
| sorted              | sorted        |                                                                                          |
| peek                | peek          |                                                                                          |
| limit               | limit         |                                                                                          |
| skip                | skip          |                                                                                          |
| takeWhile           | take_while    |                                                                                          |
| dropWhile           | drop_while    |                                                                                          |
| forEach             | for_each      |                                                                                          |
| reduce              | reduce        |                                                                                          |
| count               | count         |                                                                                          |
| min                 | min           |                                                                                          |
| max                 | max           |                                                                                          |
| findAny             | find_first    | findAny 可用 findFirst 代替                                                              |
| findFirst           | find_first    |                                                                                          |
| anyMatch            | any_match     |                                                                                          |
| noneMatch           | none_match    |                                                                                          |
| allMatch            | all_match     |                                                                                          |
| of                  | of            |                                                                                          |
| empty               | -             | 我在业务中没用过这个方法，如果有需要我会提供                                             |
| iterate             | -             | 不常用，不会提供                                                                         |
| generate            | -             | 不常用，不会提供                                                                         |
| concat              | -             | 不常用，不会提供                                                                         |
| mapToInt            | -             | 不提供                                                                                   |
| mapToLong           | -             | 不提供                                                                                   |
| mapToDouble         | -             | 不提供                                                                                   |
| flatMapToInt        | -             | 不提供                                                                                   |
| flatMapToLong       | -             | 不提供                                                                                   |
| flatMapToDouble     | -             | 不提供                                                                                   |

## FAQ
