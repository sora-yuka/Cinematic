from django.core.mail import send_mail
from config.celery import app


@app.task    
def send_act_code(email, code):
    link = f'http://localhost:8000/api/v1/account/activate/{code}'
    send_mail(
        'Your user activation code',
        f'Tap this -> {link}',
        'dcabatar@gmail.com',
        [email]    
    )
    