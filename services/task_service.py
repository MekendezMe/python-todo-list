import random
import uuid
from typing import Optional

from interfaces.dtos.ITaskDTO import ITaskDTO
from interfaces.task import ITask
from interfaces.task_service_protocol import TaskServiceProtocol


def fill_tasks(count: int) -> list[ITask]:
    descriptions = [
        "Купить продукты",
        "Позвонить врачу",
        "Написать отчёт по проекту",
        "Сделать уборку в комнате",
        "Сходить в спортзал",
        "Приготовить ужин",
        "Оплатить счета за коммунальные услуги",
        "Отправить письмо коллеге",
        "Забронировать билеты на поезд",
        "Проверить почту",
        "Сделать резервную копию данных",
        "Погулять с собакой",
        "Прочитать 20 страниц книги",
        "Полить цветы",
        "Записаться на курсы английского"
    ]

    tasks = [ITask(uuid.uuid4(), random.choice(descriptions), False) for _ in range(count)]

    return tasks


class InMemoryTaskService(TaskServiceProtocol):
    def __init__(self):
        self.tasks = []

    def get_by_index(self, index: int) -> Optional[ITask]:
        return next(((i, task) for i, task in enumerate(self.tasks) if i == index - 1), None)

    def get_all(self) -> list[ITask]:
        return self.tasks

    def add(self, task: ITaskDTO) -> ITask:
        task = ITask(uuid.uuid4(), task.description, False)
        self.tasks.append(task)
        return task

    def edit(self, index: int, description: str) -> ITask:
        for i, task in enumerate(self.tasks):
            if i == index - 1:
                task.description = description
                return task

        raise ValueError(f"Задача с id {index} не найдена")

    def complete(self, index: int) -> ITask:
        for i, task in enumerate(self.tasks):
            if i == index - 1:
                task.done = True
                return task

        raise ValueError(f"Задача с id {index} не найдена")

    def delete(self, index: int) -> bool:
        initial_length = len(self.tasks)
        self.tasks = [(i, task) for i, task in enumerate(self.tasks) if i != index - 1]

        return initial_length != len(self.tasks)

