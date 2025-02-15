import unittest

from response.types.ResponseClass import ResponseSystem
from execution.building.main_config import DEV_SETTINGS, BUILD_SETTINGS

RESPONSE_SYSTEM_FOR_TESTING = ResponseSystem(DEV_SETTINGS, BUILD_SETTINGS)

class RejectionTests(unittest.TestCase):

    def RejectQuestionTest1(self):
        # Test the rejection of a question - ONLY CALLS RESPONSE SYSTEM for now
        RESPONSE_SYSTEM_FOR_TESTING.Rejection(RESPONSE_SYSTEM_FOR_TESTING.REJECTION_TYPES.QUESTION)
        pass
    
    def RejectRequestTest1(self):
        # Test the rejection of a request - ONLY CALLS RESPONSE SYSTEM for now
        RESPONSE_SYSTEM_FOR_TESTING.Rejection(RESPONSE_SYSTEM_FOR_TESTING.REJECTION_TYPES.REQUEST)
        pass
    
    def RejectErrorTest1(self):
        # Test the rejection of an error - ONLY CALLS RESPONSE SYSTEM for now
        RESPONSE_SYSTEM_FOR_TESTING.Rejection(RESPONSE_SYSTEM_FOR_TESTING.REJECTION_TYPES.ERROR)
        pass