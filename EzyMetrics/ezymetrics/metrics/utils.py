from django.core.mail import send_mail

def send_alert_email(subject, message):
    send_mail(
        subject,
        message,
        '',
        [''],
        fail_silently=False,
    )