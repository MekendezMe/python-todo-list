import uuid

import pytest

from interfaces.dtos.ITaskDTO import ITaskDTO
from interfaces.task import ITask
from services.task_service import InMemoryTaskService
# Positive TESTS

@pytest.fixture
def task_service():
    return InMemoryTaskService()

def test_add(task_service):
    expected_task = ITask(uuid.uuid4(), description="Тест", done=False)
    actual_task = task_service.add(ITaskDTO(description="Тест"))
    assert (actual_task.description == expected_task.description
            and actual_task.done == expected_task.done)

def test_update(task_service):
    expected_task = ITask(uuid.uuid4(), description="ТестНовый", done=False)
    new_task = task_service.add(ITaskDTO(description="Тест"))
    actual_task = task_service.edit(index=1, description="ТестНовый")
    assert (actual_task.description == expected_task.description
            and actual_task.done == expected_task.done)

def test_delete(task_service):
    new_task = task_service.add(ITaskDTO(description="Тест"))
    task_deleted = task_service.delete(index=1)
    assert task_deleted == True and len(task_service.get_all()) == 0

def test_get_all(task_service):
    expected_tasks = [ITask(uuid.uuid4(), description="Тест"),
                      ITask(uuid.uuid4(), description="Тест1")]
    first_task = task_service.add(ITaskDTO(description="Тест"))
    second_task = task_service.add(ITaskDTO(description="Тест1"))
    actual_tasks = task_service.get_all()
    assert len(expected_tasks) == len(actual_tasks)

def test_get_by_index(task_service):
    expected_task = ITask(uuid.uuid4(), description="ТестПоID", done=False)
    first_task = task_service.add(ITaskDTO(description="ТестПоID"))
    actual_task = task_service.get_by_index(index=1)
    assert actual_task.description == expected_task.description

def test_complete(task_service):
    expected_task = ITask(uuid.uuid4(), description="Выполнена", done=True)
    first_task = task_service.add(ITaskDTO(description="Выполнена"))
    actual_task = task_service.complete(index=1)
    assert actual_task.done == expected_task.done
