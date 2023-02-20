import json
from django.core.management.base import BaseCommand
from People.models import Person

class Command(BaseCommand):
    help = "Load data from a JSON file"

    def add_arguments(self, parser):
        parser.add_argument('./fixtures/mock_data.json', type=str)

    def handle(self, *args, **options):
        with open(options['./fixtures/mock_data.json'], 'r') as f:
            data = json.load(f)

            for obj in data:
                my_model = Person(**obj)
                my_model.save()
                    