from platform import system
from operations.universal.abstracts import OSFunction
import pathlib
import os
import sys
import inspect
import json


class Interoperability():
    def __init__(self):
        root_path = pathlib.Path(os.path.abspath("ENTRY.py")).parent
        self.functions = {}
        self.system = system()
        osfunctions = None
        if self.system == "Windows":
            import operations.windows.osfunctions
            json_path = root_path / pathlib.Path("operations/windows/osfunctions.json")
            with open(json_path, 'r') as file:
                osfunctions = json.load(file)

        for osfunction in osfunctions:
            osf = OSFunction.from_dict(osfunction)

            class_modules = None
            if self.system == "Windows":
                class_modules = inspect.getmembers(sys.modules["operations.windows.osfunctions"], inspect.isclass)

            for module in class_modules:
                if module[0] == osf.name:
                    osf.class_object = module[1]
            
            self.functions[osf.name] = osf


    def add_function(self, function: OSFunction):
        self.functions[function.name] = function

    def get_all_functions(self) -> dict[str, OSFunction]:
        return self.functions
    
    def get_function(self, name: str) -> OSFunction:
        return self.functions.get(name)
    
    def execute_function(self, name: str, *args) -> bool:
        if len(args) != len(self.functions[name].arguments_list):
            return False
        elif self.functions[name].class_object is None:
            return False
        return self.functions[name].class_object(*args).execute()
    