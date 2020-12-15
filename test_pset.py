#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pset_6` package."""

from django.test import TestCase
from yelp_reviews.models import models, DimDate, FactReview
import unittest
from django.test import TestCase
from yelp_reviews.models import FactReview, DimDate


# Create your tests here.

class SimpleDBTest(TestCase):
    def test_basic_db(self):
        print("simple test")
        self.assertEqual(1+1,2)
        a=FactReview.objects.all()
        b=DimDate.objects.all()
        self.assertEqual(a.count(),b.count())

class SimpleTest:
    def test_basic_additions(self):
        print("Simpletest")
        self.assertEqual(1+1,2)

class TestWithUnittest(unittest.TestCase):
    def test_sample(self):
        none_variable = None

        self.assertEqual(3, 3)
        self.assertNotEqual(4, 5)
        self.assertTrue(True)
        self.assertNotIn(1, [2, 3, 4])
        self.assertIsNone(none_variable)

class TestWithPytest:
    def test_sample(self):
        none_variable = None

        assert 3 == 3
        assert 4 != 5
        assert True
        assert 1 not in [2, 3, 4]
        assert none_variable is None



#
#
# class SimpleTest(TestCase):
#     def test_field_update(self):
#         old_date = date(2012,11,11)
#         current_date = datetime.today().date()
#
#         t2 = Test2(date = old_date)
#         t2.save()
#
#         t1 = Test(test2 = t2)
#         t1.save()
#
#
#         for test_obj in Test.objects.all():
#             test2_obj = test_obj.test2
#             test2_obj.date = current_date
#             test2_obj.save()
#             test_obj.save()
#
#         t2 = Test2.objects.all()[0]
#
#         self.assertEqual(t2.date, current_date)

class FakeFileFailure(IOError):
    pass

