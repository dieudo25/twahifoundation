from django.contrib.auth import get_user
from django.db.models import Q
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy

from message.forms.message import MessageCreateUpdateForm

from account.permissions.group import GroupRequiredMixin
from account.models.user import User
from message.models.message import Message


class MessageDeleteView(GroupRequiredMixin, DeleteView):
    "Message Delete View"

    model = Message
    group_required = [u'Administrator', u'Member']
    template_name = 'message/message/delete.html'
    context_object_name = 'message'
    success_url = reverse_lazy('message:trash')


class MessageCreateView(GroupRequiredMixin, CreateView):
    "Message create view"

    model = Message
    group_required = [u'Administrator', u'Member']
    template_name = 'message/message/create.html'
    form_class = MessageCreateUpdateForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("message:outbox-detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # perform a action here
        current_user = get_user(self.request)
        form.instance.sender_id = current_user.pk
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super(MessageCreateView, self).get_form(form_class)
        current_user = get_user(self.request)
        form.fields['recipient'].queryset = User.objects.filter(
            ~Q(id=current_user.id)
        )
        return form
