from dataclasses import dataclass
from typing import Protocol

@dataclass
class ITask:
    id: int
    description: str
    done: bool