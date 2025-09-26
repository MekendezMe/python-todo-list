from pydoc import describe

from interfaces.dtos.ITaskDTO import ITaskDTO
from interfaces.task import ITask
from services.task_service import InMemoryTaskService

task_service = InMemoryTaskService()

def todo_start():
    print("Меню:\n1. Добавить задачу\n2. Показать список задач\n"
          "3. Показать задачу по номеру"
          "\n4. Изменить задачу\n5. Удалить задачу\n6. Выполнить задачу")

    user_choice = get_user_choice()

    if user_choice == 1:
        description = input("Введите задачу: ")
        if len(description) == 0:
            print("Описание должно быть заполнено")
            return

        task = task_service.add(task=ITaskDTO(description=description, done=False))
        print(f"Задача с id {task.id} успешно создана")
    elif user_choice == 2:
        tasks = task_service.get_all()
        if len(tasks) == 0:
            print("Записей нет")
            return
        for i, task in enumerate(tasks):
            print(f"Задача №{i + 1}:\nОписание: {task.description}"
                  f"\nСтатус: {"Не выполнена" if not task.done else "Выполнена"}")
    elif user_choice == 3:
        try:
            index = int(input("Введите номер задачи: "))
        except ValueError:
            print("Некорректно введен номер задачи")
            raise
        index, task = task_service.get_by_index(index)
        if task is None:
            print("Задача с данным номером не найдена")
            return
        print(f"Описание: {task.description}"
              f"\nСтатус: {"Не выполнена" if not task.done else "Выполнена"}")
    elif user_choice == 4:
        try:
            index = int(input("Введите номер задачи, которую необходимо изменить: "))
        except ValueError:
            print("Некорректно введен номер задачи")
            raise

        new_description = input("Введите новое описание задачи: ")
        if len(new_description) == 0:
            print("Описание должно быть заполнено")
            return

        try:
            task = task_service.edit(index=index, description=new_description)
            print(f"Задача с номером {index} успешно изменена."
                  f" Новое описание: {task.description}")
        except ValueError:
            print(f"Задача с номером {index} не найдена")
            return
    elif user_choice == 5:
        try:
            index = int(input("Введите номер задачи, которую необходимо удалить: "))
        except ValueError:
            print("Некорректно введен номер задачи")
            raise
        is_deleted = task_service.delete(index)
        print("Запись удалена"
              if is_deleted else "Запись с указанным номером не найдена")
    else:
        try:
            index = int(input("Введите номер задачи, которую необходимо выполнить: "))
        except ValueError:
            print("Некорректно введен номер задачи")
            raise
        is_completed = task_service.complete(index)
        print("Запись помечена как выполненная"
              if is_completed else "Запись с указанным номером не найдена")

def get_user_choice() -> int:
    try:
        user_choice: int = int(input("Введите пункт меню от 1 до 6: "))
        return user_choice
    except ValueError:
        print("Введено некорректное значение")
        raise


while True:
    todo_start()