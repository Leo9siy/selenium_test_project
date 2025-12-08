from django.core.management import BaseCommand

from scrat import utils


class Command(BaseCommand):
    def handle(self, *args, **options):
        utils.save_to_db()
