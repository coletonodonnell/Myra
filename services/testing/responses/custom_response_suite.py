import unittest

import unittest

from response.types.ResponseClass import ResponseSystem
from execution.building.main_config import DEV_SETTINGS, BUILD_SETTINGS

RESPONSE_SYSTEM_FOR_TESTING = ResponseSystem(DEV_SETTINGS, BUILD_SETTINGS)

class CustomResponseTest(unittest.TestCase):
    def setUp(self):
        print("\nSetting up suite...")
        pass
    
    def tearDown(self):
        print("Tearing down Suite...")
        pass
    
    def CustomResponseTest1(self):
        # Baseline Test
        RESPONSE_SYSTEM_FOR_TESTING.Custom_Response("Hello World!")
        self.assertTrue(True)