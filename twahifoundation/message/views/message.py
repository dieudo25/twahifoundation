from django.contrib import auth
from django.db.models import Q
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy

from message.models.message import Message

from message.forms.message import MessageCreateUpdateForm


class MessageDeleteView(DeleteView):
    "Message Delete View"

    model = Message
    template_name = 'message/message/delete.html'
    context_object_name = 'message'
    success_url = reverse_lazy('message:message-trash')


class MessageCreateView(CreateView):
    "Message create view"

    model = Message
    template_name = 'message/message/create.html'
    form_class = MessageCreateUpdateForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("message:inbox-detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # perform a action here
        current_user = auth.get_user(self.request)
        form.instance.sender_id = current_user.pk
        return super().form_valid(form)
