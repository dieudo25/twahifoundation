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
            'title_fr',
            'title_en',
            'meta_description',
            'description',
            'description_fr',
            'description_en',
            'content',
            'content_fr',
            'content_en',
            'tags',
            'keywords',
            'image',
        ]
        """ labels = {
            'title': _('Title [en]'),
            'description': _('Description [en]'),
            'content': _('Content [en]'),
        } """
class PostAllCreateUpdateForm(forms.ModelForm):
    """PostCreateForm custom made class"""

    class Meta:
        """Meta definition of PostCreateForm"""

        model = Post
        fields = [
            'title',
            'description',
            'content',
        ]
        labels = {
            'title': 'Title',
            'description': "Description",
            'content': 'Content',
        }

class PostFRCreateUpdateForm(forms.ModelForm):
    """PostCreateForm custom made class"""

    class Meta:
        """Meta definition of PostCreateForm"""

        model = Post
        fields = [
            'title_fr',
            'description_fr',
            'content_fr',
        ]
        labels = {
            'title': 'Title [fr]',
            'description': "Description [fr]",
            'content': 'Content [fr]',
        }

class PostENCreateUpdateForm(forms.ModelForm):
    """PostCreateForm custom made class"""

    class Meta:
        """Meta definition of PostCreateForm"""

        model = Post
        fields = [
            'title_en',
            'description_en',
            'content_en',
        ]
        labels = {
            'title': 'Title [en]',
            'description': "Description [en]",
            'content': 'Content [en]',
        }

class PostMultiLNCreateUpdateForm(forms.ModelForm):
    """PostCreateForm custom made class"""

    class Meta:
        """Meta definition of PostCreateForm"""

        model = Post
        fields = [
            'meta_description',
            'tags',
            'keywords',
            'image',
        ]


class PageCreateUpdateForm(forms.ModelForm):
    """PostCreateForm custom made class"""

    class Meta:
        """Meta definition of PostCreateForm"""

        model = Post
        fields = [
            'title',
            'title_fr',
            'title_en',
            'meta_description',
            'content',
            'content_fr',
            'content_en',
            'tags',
            'keywords',
        ]
        """ labels = {
            'title': _('Title [en]'),
            'content': _('Content [en]'),
        } """
