from django.core.mail import send_mail
from config.celery import app
from decouple import config


@app.task    
def send_act_code(email, code):
    link = f'http://{config("SERVER_IP")}/api/v1/account/activate/{code}'
    send_mail(
        'Your user activation code',
        f'Tap this -> {link}',
        config('EMAIL_HOST_USER'),
        [email]    
    )
    
    
@app.task    
def send_password_confirm_code(email):
    full_link = f'http://{config("SERVER_IP")}/api/v1/account/forgot_password_finish/'
    send_mail(
        'Password recovery',
        f'Tap this link-> {full_link}',
        config('EMAIL_HOST_USER'),
        [email],
    )

    