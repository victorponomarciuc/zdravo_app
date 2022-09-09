import requests
from main.models import ContactsInformation


def mailer_function(data, form_type):
    # return requests.post(
    #     "https://api.mailgun.net/v3/sandbox4112a45a64ac4706b92e3e33757986d2.mailgun.org/messages",
    #     auth=("api", "03c1049a6574c71e7991f575e9a28d4d-2bab6b06-5360ca3e"),
    #     data={"from": "zdravo.info@ukr.net",
    #           "to": "podumam@gmail.com",
    #           "subject": "Новая заявка с формы " + form_type,
    #           "text": str(data)})

    return requests.post(
        "https://api.mailgun.net/v3/sandbox2ddeaa5f0f034f5aac75b61ac62b2542.mailgun.org/messages",
        auth=("api", "9379fbf556666b9c3eca7f43de3fe644-c76388c3-1e1fca03"),
        data={"from": "zdravo.info@ukr.net",
              "to": "zdravo.inf@gmail.com",
              "subject": "Новая заявка с формы " + form_type,
              "text": str(data)})

def telegram_bot_sendtext(bot_message):
    contact = ContactsInformation.objects.last()
    bot_token = contact.telegram_token
    bot_chatID = contact.tg_chat_id
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + str(
        bot_message)
    response = requests.get(send_text)
    return response.json()
