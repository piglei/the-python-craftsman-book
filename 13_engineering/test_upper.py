# -*- coding: utf-8 -*-
import unittest


class TestStringUpper(unittest.TestCase):
    def test_normal(self):
        self.assertTrue(1)
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertGreaterEqual

    def test_normal2(self):
        self.assertEqual('foo'.upper(), 'FOO333')
        self.assertGreaterEqual


if __name__ == '__main__':
    unittest.main()