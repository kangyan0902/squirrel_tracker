from django.core.management.base import BaseCommand, CommandError
from sighting.models import Squirrel
from django.apps import apps

class Command(BaseCommand):
    help = 'exports all information to csv files'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        with open(kwargs['path'], 'w', newline='') as csvfile:
            attributes = ['Latitude', 
            			'Longitude', 
            			'Unique_Squirrel_id', 
            			'Shift', 
            			'Date', 
            			'Age', 
            			'Fur_Color', 
            			'Location',
                        'Specific_Location',
                        'Running',
                        'Chasing',
                        'Climbing',
                        'Eating',
                        'Foraging',
                        'Other_Activities',
                        'Kuks',
                        'Quaas',
                        'Moans',
                        'Tail_Flags',
                        'Tail_Twitches',
                        'Approaches',
                        'Indifferent',
                        'Runs_From']
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow(names)
            for row in Squirrel.objects.all():
                writer.writerow([getattr(row, attribute) for attribute in attributes])