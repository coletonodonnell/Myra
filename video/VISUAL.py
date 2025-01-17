from execution.teardown.teardown import Shutdown_Assistant

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