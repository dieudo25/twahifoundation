import json
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

list_id = "edee4d8450"
api_key = "66769690f357618ee67b830b0c866947-us17"
server = "us17"

try:
    client = MailchimpMarketing.Client()
    client.set_config({
        "api_key": api_key,
        "server": server
    })

    response = client.lists.get_list_members_info(list_id)

    print(json.dumps(response, indent=3))

except ApiClientError as error:
    print("Error: {}".format(error.text))
