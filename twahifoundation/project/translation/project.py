from modeltranslation.translator import translator, TranslationOptions
from project.models.project import Project


class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content', )


translator.register(Project, ProjectTranslationOptions)
