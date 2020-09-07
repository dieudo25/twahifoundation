from django import forms


from message.models.message import Message


class MessageCreateUpdateForm(forms.ModelForm):
    """MessageCreateForm custom made class"""

    class Meta:
        """Meta definition of MessageCreateForm"""

        model = Message
        fields = [
            'recipient',
            'subject',
            'body',
            'uploaded_file',
        ]
