# Teardown File ----------------------------------------------
# To safely shut down the assistant and clean up any resources.
# We don't want to break the user's system by leaving any resources open
# and whatnot. Make sure to call this any time the assistant is closed.
#
# Current Teardown Tasks:
# 1. Close the assistant's visual component (TO DO)
# 
# 
#
#
# -----------------------------------------------------

import os


def Shutdown_Assistant():
    print("Shutting down the assistant...")
    
    
    # Forceful exit bc sys.exit() doesn't work with eel for some reason
    os._exit(0)
   
    pass