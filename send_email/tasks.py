from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from sprint import settings
# from django.utils import timezone
from datetime import datetime
from users import models

@shared_task(bind=True)
def send_email_func(self): 
    users = models.Profile.objects.all()
    for user in users:
        if user.tipo_usuario == 'Bolsista':
            if ((datetime.now() - user.ultima_atualizacao.replace(tzinfo=None)).days / 30.417) >= 6 and int(user.ano_formatura) != (datetime.now().year):
                mail_subject = "Olá Bolsista!"
                message = """
                <!DOCTYPE html>
                    <html>
                        <h1>Olá Bolsista!</h1>
                        <p>Segue o aviso para a atualização de seu Histórico Acadêmido!</p>
                    </html>
                """
                
                to_email = user.email
                send_mail(
                subject = mail_subject,
                message = message,
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [to_email],
                fail_silently = True
                )
            
            elif ((datetime.now() - user.ultima_atualizacao.replace(tzinfo=None)).days / 30.417) >= 6 and int(user.ano_formatura) == (datetime.now().year):
                mail_subject = "Olá Bolsista!"
                message = """
                <!DOCTYPE html>
                    <html>
                        <h1>Olá Bolsista!</h1>
                        <p>Segue o aviso para a atualização de seu Histórico Acadêmido!</p>
                        <p>Lembre de avisar a Intituição se seu ano previsto para formatura continua o mesmo, caso não continue, informe o novo ano previsto de formatura.</p>
                    </html>
                """
                to_email = user.email
                send_mail(
                subject = mail_subject,
                message = message,
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [to_email],
                fail_silently = True
                )
    
        elif user.tipo_usuario == 'Alumni':
            if ((datetime.now() - user.ultima_atualizacao.replace(tzinfo=None)).days / 30.417) >= 6:
                mail_subject = "Olá Alumni!"
                message = """
                <!DOCTYPE html>
                    <html>
                        <h1>Olá Alumni!</h1>
                        <p>Segue o aviso para a atualização de seu Histórico Profissional!</p>
                    </html>
                """
                to_email = user.email
                send_mail(
                subject = mail_subject,
                message = message,
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [to_email],
                fail_silently = True
                )

    return "E-mail de cadastro enviado!"