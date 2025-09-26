import random
import uuid
from typing import Optional

from exceptions.description_not_filled_exception import DescriptionNotFilledException
from exceptions.task_not_found_exception import TaskNotFoundException
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
        return self.tasks[index - 1] if 0 < index <= len(self.tasks) else None

    def get_all(self) -> list[ITask]:
        return self.tasks

    def add(self, task: ITaskDTO) -> ITask:
        if len(task.description) == 0:
            raise DescriptionNotFilledException()

        task = ITask(uuid.uuid4(), task.description, False)
        self.tasks.append(task)
        return task

    def edit(self, index: int, description: str) -> ITask:
        if len(description) == 0:
            raise DescriptionNotFilledException()

        for i, task in enumerate(self.tasks):
            if i == index - 1:
                task.description = description
                return task

        raise TaskNotFoundException(f"Задача с id {index} не найдена")

    def complete(self, index: int) -> ITask:
        for i, task in enumerate(self.tasks):
            if i == index - 1:
                task.done = True
                return task

        raise TaskNotFoundException(f"Задача с id {index} не найдена")

    def delete(self, index: int) -> bool:
        if 0 < index <= len(self.tasks):
            del self.tasks[index - 1]
            return True
        return False

