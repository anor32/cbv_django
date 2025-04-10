from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings

class Command(BaseCommand):
    help = 'Send a test email'

    def handle(self, *args, **kwargs):
        try:
            send_mail(
                subject="Test Email",
                message="This is a test email from Django.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["input_mail@here"],
            )
            self.stdout.write(self.style.SUCCESS("Email sent successfully!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))