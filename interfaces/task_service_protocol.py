from typing import Protocol

from interfaces.dtos.ITaskDTO import ITaskDTO
from interfaces.task import ITask


class TaskServiceProtocol(Protocol):
    def get_all(self) -> list[ITask]:
        ...

    def get_by_index(self, index: int) -> ITask:
        ...

    def add(self, task: ITaskDTO) -> ITask:
        ...

    def edit(self, index: int, description: str) -> ITask:
        ...

    def complete(self, index: int) -> ITask:
        ...

    def delete(self, index: int) -> bool:
        ...