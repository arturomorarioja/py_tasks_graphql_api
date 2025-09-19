from graphene import ObjectType, String, Boolean


class Task(ObjectType):
    title = String()
    completed = Boolean()