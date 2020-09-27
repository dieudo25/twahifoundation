from django import forms
from django.utils.translation import ugettext_lazy as _

from blog.models.post import Post


class PostCreateUpdateForm(forms.ModelForm):
    """PostCreateForm custom made class"""

    class Meta:
        """Meta definition of PostCreateForm"""

        model = Post
        fields = [
            'title',
            'meta_description',
            'description',
            'content',
            'tags',
            'keywords',
            'image',
        ]
        labels = {
            'title': _('Title [en]'),
            'description': _('Description [en]'),
            'content': _('Content [en]'),
        }


class PageCreateUpdateForm(forms.ModelForm):
    """PostCreateForm custom made class"""

    class Meta:
        """Meta definition of PostCreateForm"""

        model = Post
        fields = [
            'title',
            'meta_description',
            'content',
            'tags',
            'keywords',
        ]
        labels = {
            'title': _('Title [en]'),
            'content': _('Content [en]'),
        }
