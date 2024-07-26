from dataclasses import dataclass
from typing import Optional


@dataclass
class Person:
    name: str
    age: int
    city: Optional[str] = None

