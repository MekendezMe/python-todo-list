from dataclasses import dataclass
from typing import Optional


@dataclass
class ITaskDTO:
    description: str
    done: Optional[bool] = False