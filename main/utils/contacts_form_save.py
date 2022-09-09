from main.models import *
from main.utils.alert_mail_tg import mailer_function, telegram_bot_sendtext


def contact_form_save(data):
    order = ContactForm()
    order_comment = ''
    try:
        client = Clients.objects.get(phone=data['phone'])
        if client.name != data['firstname']:
            client_comment = "С этого номера записался еще и клиент " + data['firstname']
            order_comment = "С этого номера записался клиент " + data['firstname'] + " Под этим номером зарегистрирован клиент " + client.name
            try:
                client.comment = client.comment + "\n" + client_comment
            except:
                client.comment = client.comment + " ошибка!!!!!"
            client.save()
            order.comment = order_comment
    except:
        client = Clients()
        client.name = data['firstname']
        client.last_name = ''
        client.phone = data['phone']
        client.mail = ''
        client.save()
    order.client = client
    order.date_created = datetime.date.today()
    order.save()
    mail_data = "Заявка: Общая Консультация" + "\n" + "Номер заявки: " + str(order.pk) + "\n" + "ФИО: " + data[
        'firstname'] + "\n" + "Телефон: " + \
                data[
                    'phone'] + "\n" + "Комментарий: " + order_comment
    mailer_function(mail_data, 'Контакты')
    telegram_bot_sendtext(mail_data)
