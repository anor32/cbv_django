from django.conf import settings
from django.core.mail import send_mail

def send_register_email(email):
    send_mail(
        subject = "Поздравляем с регистрация на нашем сервере ",
        message = "Вы Успешно Зарегитсриовались на плафторме WEB426FBVShelter",
        from_email= settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
def send_new_password(email,new_password):
    send_mail(
        subject="ВЫ успешно изменили пароль ",
        message=f"Ваш Новый пароль {new_password}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
