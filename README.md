# [Python dataclasses](https://docs.python.org/3/library/dataclasses.html)

Python 提供 dataclasses module 用于序列化。默认的 dataclass 可以从字典和数组等结构中构造出 class 对象。  

默认的 dataclass 不支持额外字段（会抛出 TypeError 异常），不支持缺少字段（使用默认值 None 可以做到）。想要做到忽略额外字段，需要自己重写`__init__`方法自行过滤。重写的`__init__`方法，既要过滤多余字段，还需要检查非可选择字段的完整性（抛出异常）。

```shell
python -m unittest discover -s tests
```