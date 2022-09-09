from main.models import *
from main.utils.alert_mail_tg import mailer_function, telegram_bot_sendtext


def service_online_form_save(data):
    order = ServiceForm()
    service = Services.objects.get(pk=data['service_id'])
    try:
        client = Clients.objects.get(phone=data['phone'])
        if client.name != data['firstname']:
            order.comment = data['comment'] + "\n" + "\n" + "С этого номера записался клиент " + data[
                'firstname'] + " Под этим номером зарегистрирован клиент " + client.name
        else:
            order.comment = data['comment']
    except:
        client = Clients()
        client.name = data['firstname']
        client.last_name = ''
        client.phone = data['phone']
        client.mail = ''
        client.save()
        order.comment = data['comment']
    order.client = client
    order.date_created = datetime.date.today()
    order.service = service
    order.service_type = data['service_type']
    order.save()
    mail_message = "Заявка: " + service.title + "\n" + "Номер заявки: " + str(order.pk) + "\n" + "Тип заявки: " + data[
        'service_type_name'] + "\n" + "ФИО: " + data[
                       'firstname'] + "\n" + "Телефон: " + data[
                       'phone'] + "\n" + "Комментарий: " + data['comment']
    mailer_function(mail_message, 'Онлайн Запись')
    telegram_bot_sendtext(mail_message)


def reg_online_simple(data):
    order = ServiceForm()
    try:
        client = Clients.objects.get(phone=data['phone'])
        if client.name != data['firstname']:
            order.comment = data['comment'] + "\n" + "\n" + "С этого номера записался клиент " + data[
                'firstname'] + " Под этим номером зарегистрирован клиент " + client.name
        else:
            order.comment = data['comment']
    except:
        client = Clients()
        client.name = data['firstname']
        client.last_name = ''
        client.phone = data['phone']
        client.mail = ''
        client.save()
        order.comment = data['comment']
    order.client = client
    order.service = Services.objects.get(slug='onlain-zapis')
    order.date_created = datetime.date.today()
    order.save()
    mail_message = "Заявка: Онлайн запись " + "\n" + "Номер заявки: " + str(order.pk) + "\n" + "ФИО: " + data[
        'firstname'] + "Телефон: " + data[
                       'phone'] + "\n" + "Комментарий: " + data['comment']
    mailer_function(mail_message, 'Онлайн Запись')
    telegram_bot_sendtext(mail_message)
