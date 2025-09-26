import uuid
from dataclasses import dataclass
from typing import Protocol, Optional


@dataclass
class ITask:
    id: uuid.UUID
    description: str
    done: Optional[bool] = False