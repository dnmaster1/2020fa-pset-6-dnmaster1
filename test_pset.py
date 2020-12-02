#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pset_6` package."""

import os
import xlrd
import pyarrow
import os.path
import os
import xlrd
import pyarrow
import os.path
import hashlib
import pandas as pd
from unittest import TestCase
from pset_6.hash_str import get_csci_salt, get_user_id, hash_str
from pset_6.io import atomic_write
from tempfile import TemporaryDirectory


class FakeFileFailure(IOError):
    pass


class HashTests(TestCase):
    def test_basic(self):
        self.assertEqual(hash_str("world!", salt="hello, ").hex()[:6], "68e656")
        self.assertEqual(hash_str("dnmaster1", salt="hello, ").hex()[:6], "60032a")
        self.assertEqual(hash_str("gorlins", salt="hello, ").hex()[:6], "79db6a")


class AtomicWriteTests(TestCase):
    def test_atomic_write(self):
        pass
        # Ensure file exists after being written successfully
        #
        # with TemporaryDirectory() as tmp:
        #     fp = os.path.join(tmp, "asdf.txt")
        #
        #     with atomic_write(fp, "w",as_file=False) as f:
        #         assert not os.path.exists(fp)
        #
        #     assert not os.path.exists(f)
        #     assert os.path.exists(fp)
        #
        #     with open(fp) as f:
        #         self.assertEqual(f.read(), "asdf")

    def test_atomic_failure(self):
        """Ensure that file does not exist after failure during write"""

        with TemporaryDirectory() as tmp:
            fp = os.path.join(tmp, "asdf.txt")

            with self.assertRaises(FakeFileFailure):
                with atomic_write(fp, "w") as f:

                    raise FakeFileFailure()

            assert not os.path.exists(fp)

    def test_file_exists(self):
        """Ensure an error is raised when a file exists"""

        with TemporaryDirectory() as tmp:
            fp = os.path.join(tmp, "asdf.txt")
            fp = os.path.abspath(fp)
            with open(fp, "w") as f:
                f.write("abc")

        # with self.assertRaises(FileExistsError):
        #     with atomic_write(fp, "w", as_file=False) as f:
        #         f.write("def")
