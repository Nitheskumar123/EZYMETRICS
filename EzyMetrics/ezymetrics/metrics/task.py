from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_notification(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        'nithes262004@gmail.com',  
        recipient_list,
        fail_silently=False,
    )