from typing import Protocol

from interfaces.dtos.ITaskDTO import ITaskDTO
from interfaces.task import ITask


class TaskServiceProtocol(Protocol):
    def get_all(self) -> list[ITask]:
        ...

    def get_by_id(self, id: int) -> ITask:
        ...

    def add(self, task: ITaskDTO) -> ITask:
        ...

    def edit(self, task: ITask) -> ITask:
        ...

    def complete(self, id: int) -> ITask:
        ...

    def delete(self, id: int) -> bool:
        ...