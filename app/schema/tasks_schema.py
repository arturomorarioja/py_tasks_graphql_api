from graphene import ObjectType, String, List, Field, Schema, Mutation, Boolean, Argument
from ..data.tasks_store import tasks_data


class Task(ObjectType):
    title = String()
    completed = Boolean()


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


class AddTask(Mutation):
    class Arguments:
        title = String(required=True)

    success = Boolean()
    task = Field(lambda: Task)

    def mutate(root, info, title):
        new_entry = {'title': title, 'completed': False}
        tasks_data.append(new_entry)
        return AddTask(success=True, task=Task(**new_entry))


class UpdateTask(Mutation):
    class Arguments:
        title = String(required=True)
        new_title = String(name='newTitle', required=False)
        completed = Boolean(required=False)

    success = Boolean()
    task = Field(lambda: Task)

    def mutate(root, info, title, new_title=None, completed=None):
        for t in tasks_data:
            if t['title'] == title:
                if new_title is not None:
                    t['title'] = new_title
                if completed is not None:
                    t['completed'] = completed
                return UpdateTask(success=True, task=Task(title=t['title'], completed=t['completed']))
        return UpdateTask(success=False, task=None)


class DeleteTask(Mutation):
    class Arguments:
        title = String(required=True)

    success = Boolean()
    deleted_task = Field(lambda: Task, name='deletedTask')

    def mutate(root, info, title):
        for i, t in enumerate(tasks_data):
            if t['title'] == title:
                removed = tasks_data.pop(i)
                return DeleteTask(success=True, deleted_task=Task(**removed))
        return DeleteTask(success=False, deleted_task=None)


class Mutation(ObjectType):
    add_task = AddTask.Field()
    update_task = UpdateTask.Field()
    delete_task = DeleteTask.Field()


schema = Schema(query=Query, mutation=Mutation)