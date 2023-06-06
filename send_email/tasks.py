from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from sprint import settings
# from django.utils import timezone
from datetime import timedelta, datetime

@shared_task(bind=True)
def send_email_func(self):
    users = get_user_model().objects.all()
    # timezone.localtime(users.date_time) + timedelta(days = 2)
    for user in users:

        # if user.ano_formatura == (datetime.now().year):
            mail_subject = "Olá Bolsista!"
            message = 'Segue o link para reenvio semestral de seu histórico' + ' ' + 'http://127.0.0.1:8000/accounts/profile/history/school'
            to_email = user.email
            send_mail(
            subject = mail_subject,
            message = message,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [to_email],
            fail_silently = True
            )

        # else:
        #     mail_subject = "Olá Bolsista!"
        #     message = 'Segue o link para reenvio semestral de seu histórico' + ' ' + 'http://127.0.0.1:8000/accounts/profile/history/school'
        #     to_email = user.email
        #     send_mail(
        #     subject = mail_subject,
        #     message = message,
        #     from_email = settings.EMAIL_HOST_USER,
        #     recipient_list = [to_email],
        #     fail_silently = True
        #     )
    
    return "E-mail de cadastro enviado!"