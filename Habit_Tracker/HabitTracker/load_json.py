import json
from django.core.management.base import BaseCommand
from HabitTracker.models import Person

class Command(BaseCommand):
    help = 'Load data from a JSON file'
    def add_arguments(self,parser):
        parser.add_argument('../test_data.json', type=str)
        
    def handle(self, *args, **options):
        with open(options['../test_data.json'], 'r') as f:
            data = json.load(f)
            
            for obj in data:
                name = obj.get('name')
                username = obj.get('username')
                habit = obj.get('habit')
                
                if name and username and habit:
                    my_model = Person(**obj)
                    my_model.save()
