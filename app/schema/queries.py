from graphene import ObjectType, String, List, Field, Argument
from .types import Task
from ..data.tasks_store import tasks_data


class Query(ObjectType):
    # task(title): returns a single Task
    # tasks: returns a list of all tasks
    task = Field(lambda: Task, title=Argument(String, required=True))
    tasks = List(lambda: Task)

    def resolve_task(root, info, title):
        for t in tasks_data:
            if t['title'] == title:
                return Task(title=t['title'], completed=t['completed'])
        return None

    def resolve_tasks(root, info):
        return [Task(title=t['title'], completed=t['completed']) for t in tasks_data]