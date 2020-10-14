from modeltranslation.translator import translator, TranslationOptions
from project.models.task import Task


class TaskTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


translator.register(Task, TaskTranslationOptions)
