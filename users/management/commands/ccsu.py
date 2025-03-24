
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        admin_user = User.objects.create(
            email = "admin@web.top",
            first_name = "Andrei",
            last_name = "Nikanov",
            is_staff = True,
            is_superuser = True,
            is_active = True,
            date_birth = "2000-04-30"
        )
        admin_user.set_password("querty")
        admin_user.save()
        print("admin_created")
