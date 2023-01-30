import os
import shutil

import bs4

class XMLHandler:
    
    def __init__(self, file_path):        
        self.add_if_not_exist = True
        self.file_path = file_path

    def Add(self, path, attr, value):
        pass

    def Edit(self, path, attr, value):
        pass

    def Comment(self, path):
        pass

    def UnComment(self, path):
        pass

class WebConfigFabric:
    
    DEFAULT_WEBCONFIG_BASE_FILE = "../config/base_files/Web.config"

    def __init__(self, output_dir) -> None:
        self.file_path = os.path.join(output_dir, "Web.config")
        self.__copy_base_file()
        self.xml_handler = XMLHandler

    def __copy_base_file(self):
        shutil.copy(WebConfigFabric.DEFAULT_WEBCONFIG_BASE_FILE, self.file_path)

