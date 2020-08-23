import json

from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect
from django.urls import reverse

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

list_id = settings.MAILCHIMP_EMAIL_LIST_ID
api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER


class SubsciberListView(TemplateView):

    template_name = "newsletter/subscriber/list.html"

    try:
        mailchimp = MailchimpMarketing.Client()
        mailchimp.set_config({
            "api_key": api_key,
            "server": server
        })

        response = mailchimp.lists.get_list_members_info(list_id)

        response = (response['members'])

        data_list = []

        for member in response:
            email = member["email_address"]
            status = member["status"]
            subcribed_on = member["timestamp_signup"]

            data = {
                'email': email,
                'status': status,
                'subcribed_on': subcribed_on,
            }

            data_list.append(data)

    except ApiClientError as error:
        print("Error: {}".format(error.text))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = self.data_list
        return context


""" class SubsciberAddView(TemplateView):

    template_name = "newsletter/subscriber/add.html"

    try:
        mailchimp = MailchimpMarketing.Client()
        mailchimp.set_config({
            "api_key": api_key,
            "server": server
        })

        response = mailchimp.lists.add_list_member(
            list_id, {"email_address": "twahirwa25@gmail.com", "status": "pending"})

        json_object = json.loads(response.text)
        print(json.dumps(json_object, indent=3))

    except ApiClientError as error:
        print("Error: {}".format(error.text)) """


def subscribed_add_view(request):

    if request.method == 'POST':
        email = request.POST['email']
        message_success = 'You have successfully subscribed to the newsletter.'
        message_email_exist = 'You are already subscribed to the newsletter.'
        result = ''

        try:
            mailchimp = MailchimpMarketing.Client()
            mailchimp.set_config({
                "api_key": api_key,
                "server": server
            })

            response = mailchimp.lists.get_list_members_info(list_id)

            response = (response['members'])

            data_list = []

            for member in response:
                member_email = member["email_address"]
                data_list.append(member_email)

            if email in data_list:
                result = message_email_exist
            else:
                result = message_success

            mailchimp.lists.add_list_member(
                list_id, {"email_address": email, "status": "pending"})

            """ print(json.dumps(json_object, indent=3)) """

        except ApiClientError as error:
            print("Error: {}".format(error.text))

        return render(request, 'newsletter/subscriber/add.html', {'result': result})
