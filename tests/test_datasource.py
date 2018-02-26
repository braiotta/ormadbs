import unittest.mock
from objects.DataSource import DataSource


class DatasourceTestCase(unittest.TestCase):
    def test_add_zero_to_zip(self):
        self.assertEqual('02134', DataSource.pad_zip(zip='2134'))
        self.assertEqual('02134', DataSource.pad_zip(zip='02134'))