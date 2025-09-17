from django.core.management.base import BaseCommand
from users.utils import cleanup_orphaned_user3_accounts

class Command(BaseCommand):
    help = 'Remove User3 accounts that have no attendance records'

    def handle(self, *args, **options):
        deleted_count, deleted_usernames = cleanup_orphaned_user3_accounts()
        
        if deleted_count > 0:
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully removed {deleted_count} orphaned User3 accounts: {", ".join(deleted_usernames)}'
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('No orphaned User3 accounts found.')
            )