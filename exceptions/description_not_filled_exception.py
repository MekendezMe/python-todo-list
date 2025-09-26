class DescriptionNotFilledException(Exception):
    def __init__(self, message: str = "Описание задачи не должно быть пустым"):
        super().__init__(message)