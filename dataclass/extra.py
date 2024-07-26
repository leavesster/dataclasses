from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class Person:
    name: str
    age: int
    city: Optional[str] = None

    def __init__(self, **kwargs):
        keys = self.__annotations__.keys()
        for k, v in kwargs.items():
            if k in keys: # 多余字段不处理，直接忽略
                setattr(self, k, v)
        for k in keys: # 如果缺少字段，需要报错
            if hasattr(self, k) is False:
                raise TypeError("missing field" + k)