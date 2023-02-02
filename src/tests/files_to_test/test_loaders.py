import unittest

from loader import Loader
class TestLoader(unittest.TestCase):
    SPREADSHEET = "./files_to_test/test_config.xlsx"
    JSON = "./files_to_test/test_config.json"
    
    def test_json_to_excel_lookup_table(self):
