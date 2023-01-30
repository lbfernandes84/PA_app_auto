import unittest

import sys
import os

sys.path.append("..")

from xml_configs.xml_parser import WebConfigFabric

class TestXML(unittest.TestCase):

    created_files = []    
    
    def test_copy_file(self):
        xmlfFabric = WebConfigFabric(".")    
        TestXML.created_files.append(xmlfFabric.file_path)
        self.assertTrue(os.path.exists(xmlfFabric.file_path))
    
    def tearDown(self):
        for file_ in TestXML.created_files:
            os.remove(os.path.abspath(file_))
        return super().tearDown()