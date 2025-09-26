class TaskNotFoundException(Exception):
    def __init__(self, message: str = "Задача с указанным номером не найдена"):
        super().__init__(message)