#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pset_6` package."""

from django.test import TestCase
from yelp_reviews.models import models, Test, Test2

from datetime import datetime, date

class SimpleTest(TestCase):
    def test_field_update(self):
        old_date = date(2012,11,11)
        current_date = datetime.today().date()

        t2 = Test2(date = old_date)
        t2.save()

        t1 = Test(test2 = t2)
        t1.save()


        for test_obj in Test.objects.all():
            test2_obj = test_obj.test2
            test2_obj.date = current_date
            test2_obj.save()
            test_obj.save()

        t2 = Test2.objects.all()[0]

        self.assertEqual(t2.date, current_date)

class FakeFileFailure(IOError):
    pass

