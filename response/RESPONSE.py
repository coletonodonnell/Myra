# -----------------------------------
# Response system for Myra.
# 
# This file is the high-level file that creates and manages
# the response system for Myra. It is responsible for handling
# all the responses that Myra can give to the user defined
# by the user's query. All variables changed here.
#
# Please import the GLOBAL response system object from this file.
# ---------------------------------

# Imports
from response.types.ResponseClass import ResponseSystem

from execution.building.main_config import DEV_SETTINGS, BUILD_SETTINGS


# Init the response system
RESPONSE_SYSTEM = ResponseSystem(DEV_SETTINGS, BUILD_SETTINGS)
