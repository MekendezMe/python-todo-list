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
    tasks: list[ITask]
    def __init__(self):
        self.tasks = fill_tasks(15)

    def get_by_id(self, id: int) -> Optional[ITask]:
        return next((task for task in self.tasks if task.id == id), None)

    def get_all(self) -> list[ITask]:
        return self.tasks

    def add(self, task: ITaskDTO) -> ITask:
        task = ITask(uuid.uuid4(), ITaskDTO.description, False)
        self.tasks.append(task)
        return task

    def edit(self, update_task: ITask) -> ITask:
        for task in self.tasks:
            if task.id == update_task.id:
                task.description = update_task.description
                return task

        raise ValueError(f"Задача с id {update_task.id} не найдена")

    def complete(self, id: int) -> ITask:
        for task in self.tasks:
            if task.id == id:
                task.done = True
                return task

        raise ValueError(f"Задача с id {id} не найдена")

    def delete(self, id: int) -> bool:
        new_tasks = []
        initial_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != id]

        return initial_length != len(new_tasks)

