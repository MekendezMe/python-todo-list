from dataclasses import dataclass

@dataclass
class ITaskDTO:
    description: str
    done: bool