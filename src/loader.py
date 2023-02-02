import json
from  openpyxl import load_workbook

class Loader:

    def __init__(self, spreadsheet_file_path, lookup_table_file):        
        self.spreadsheet_config = load_workbook(filename = spreadsheet_file_path)
        self.json_lookup_table =  json.loads(lookup_table_file)

    def get(self, config_path):
        pass