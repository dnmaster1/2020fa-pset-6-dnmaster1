from django.test import TestCase
import yelp_reviews.models
import yelp_reviews.models
from yelp_reviews.models import FactReview, DimDate


# Create your tests here.

class SimpleTest(TestCase):
    def test_basic_db(self):
        print("simple test")
        self.assertEqual(1+1,2)
        a=FactReview.objects.all()
        b=DimDate.objects.all()
        self.assertEqual(a.count(),b.count())
