from django.core.management import BaseCommand

from scrat.utils import save_to_db


class Command(BaseCommand):
    def handle(self, *args, **options):
        save_to_db()
