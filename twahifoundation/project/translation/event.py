from modeltranslation.translator import translator, TranslationOptions
from project.models.event import Event


class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'location', 'content', )


translator.register(Event, EventTranslationOptions)
