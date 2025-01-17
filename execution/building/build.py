# Build File ----------------------------------------------
# Any tasks that need to be done before the assistant is ready to take
# queries which improves performance or functionality.
#
# Current Build Tasks:
# 1. Set the voice of the assistant
# 2. Initialize the assistant's visual component
# 
#
#
# -----------------------------------------------------
from audio.AUDIO import Set_Voice
from execution.build.main_config import BUILD_SETTINGS, DEV_SETTINGS
from video.VISUAL import Init_Window

import threading


def Build():
  
  # Set the voice of the assistant
  Set_Voice(BUILD_SETTINGS["starterVoice"])
  
  # Initialize the assistant's visual component - Threaded to allow for concurrent execution
  if (DEV_SETTINGS["usingGUI"]):
    GUI_THREAD = threading.Thread(target=Init_Window)
    GUI_THREAD.start()
    GUI_THREAD.join(timeout=1)
    
  
  
  
  pass

