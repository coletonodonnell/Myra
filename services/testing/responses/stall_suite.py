import unittest
import time

from response.functions.Rejection import Rejection
from response.types.ResponseClass import ResponseSystem
from execution.building.main_config import DEV_SETTINGS, BUILD_SETTINGS

RESPONSE_SYSTEM_FOR_TESTING = ResponseSystem(DEV_SETTINGS, BUILD_SETTINGS)

class StallTests(unittest.TestCase):
    def StallTest1(self):
        RESPONSE_SYSTEM_FOR_TESTING.Stall()
        self.assertTrue(True)
        
    def ReturnFromStallTest1(self):
        RESPONSE_SYSTEM_FOR_TESTING.Return_From_Stall()
        self.assertTrue(True)
        
    def StallAndReturnTest1(self):
        RESPONSE_SYSTEM_FOR_TESTING.Stall()
        time.sleep(5)
        RESPONSE_SYSTEM_FOR_TESTING.Return_From_Stall()
        self.assertTrue(True)