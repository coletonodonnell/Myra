from execution.teardown.teardown import Shutdown_Assistant
from command.functions.Command_Functions import Set_New_Query_Available, Set_Current_Query

import eel

# Initialize the window for the assistant
def Init_Window():
    eel.init('./video/web')
    
    eel.start('index.html', close_callback=Shutdown_Assistant)
  
  
    pass
  
  
# Update the window with new information 
def Update():
    
    
    pass


def Close_Window():
    
    pass


@eel.expose
def Receive_Query_From_GUI(query):
    print(f"Received text query: {query}")
    
    # Set current query to the received query
    Set_Current_Query(query)
    
    # Set New Query to True - this will allow the assistant to process the query. Automatically set to False after processing
    Set_New_Query_Available(True)
    