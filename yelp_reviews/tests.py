from django.test import TestCase

# Create your tests here.

class SimpleTest(TestCase):
    def test_basi_addition(self):
        print("simple test")
        self.assertEqual(1+1,2)