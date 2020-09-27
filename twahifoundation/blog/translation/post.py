from modeltranslation.translator import translator, TranslationOptions
from blog.models.post import Post


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content', )


translator.register(Post, PostTranslationOptions)
