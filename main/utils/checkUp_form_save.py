from main.models import *
from multiprocessing import Process
from main.utils.alert_mail_tg import mailer_function, telegram_bot_sendtext


def check_up_form_save(data):
    order = CheckUPForm()
    order_comment = ''
    try:
        client = Clients.objects.get(phone=data['phone'])
        if client.name != data['firstname']:
            client_comment = "С этого номера записался еще и клиент " + data['firstname']
            order_comment = "С этого номера записался клиент " + data[
                'firstname'] + " Под этим номером зарегистрирован клиент " + client.name
            try:
                client.comment = client.comment + "\n" + client_comment
            except:
                client.comment = client.comment + " ошибка!!!!!"
            client.save()
            order.comment = data['comment'] + '\n' + order_comment
    except:
        client = Clients()
        client.name = data['firstname']
        client.phone = data['phone']
        client.mail = ''
        client.save()
    order.client = client
    order.date_created = datetime.date.today()
    order.save()
    mail_data = "Заявка: Проходження Check-up <<" + data['check_up_type'] + ">> " + "\n" + "Номер заявки: " + str(
        order.pk) + "\n" + "ФИО: " + data[
                    'firstname'] + "\n" + "Телефон: " + \
                data[
                    'phone'] + "\n" + "Комментарий: " + data[
                    'comment'] + '\n' + order_comment
    mailer_function(mail_data, "Check-up")
    telegram_bot_sendtext(mail_data)
