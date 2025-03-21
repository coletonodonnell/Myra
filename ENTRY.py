from command.QUERY import *
from services.testing.TESTING import Run_Test_Suite
from execution.building.build import *
from services.voices import create_table
from response.conversational.CONVERSATION import *

Current_Mode = "ASSISTANT"

if __name__ == "__main__":
  
  # Initialization
  Build()
  
  # Engagment Loop
  while(True):
    
    if Current_Mode == "TESTING":
      # Run the test suite if the mode is TESTING
      # Ensure the test suite is configured before use
      Run_Test_Suite()
      break
    
    
    elif Current_Mode == "ASSISTANT":

      
      # Begin the assistant's main loop to take queries
      Main_Query_Loop()
      
      # adjust later to accomodate for changing modes
      break
      
    
    elif Current_Mode == "CONVERSE":
      # Run the conversation mode
      Run_Conversation()

      break
      
      pass