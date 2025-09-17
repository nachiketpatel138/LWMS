from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Create master user for the system'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, default='master')
        parser.add_argument('--password', type=str, default='master123')
        parser.add_argument('--email', type=str, default='master@system.com')

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        email = options['email']

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'Master user "{username}" already exists')
            )
            return

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            role='master',
            is_staff=True,
            is_superuser=True,
            force_password_change=False
        )

        self.stdout.write(
            self.style.SUCCESS(f'Master user "{username}" created successfully')
        )