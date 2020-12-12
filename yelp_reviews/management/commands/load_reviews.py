from django.core.management import BaseCommand

from .models import DimDate, FactReview


class Command(BaseCommand):
    help = "Load review facts"

    def add_arguments(self, parser):
        parser.add_argument("-f", "--full", action="store_true")

    def handle(self, *args, **options):
        """Populates the DB with review aggregations"""
        # Load the data
        # Calculate daily aggregations
        # Store results into FactReview
        ...