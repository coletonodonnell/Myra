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
from execution.building.main_config import BUILD_SETTINGS, DEV_SETTINGS, HUGGINGFACE_API_KEY, LANGSMITH_API_KEY, LANGSMITH_SETTINGS
from video.VISUAL import Init_Window
from services.voices import create_table
import os


import threading


def Build():

  # Set up Huggingface API Token
  os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACE_API_KEY

  # Set up Langsmith Tracing for Myra
  os.environ["LANGSMITH_API_KEY"] = LANGSMITH_API_KEY

  os.environ["LANGSMITH_TRACING"] = LANGSMITH_SETTINGS["LANGSMITH_TRACING"]
  os.environ["LANGSMITH_ENDPOINT"] = LANGSMITH_SETTINGS["LANGSMITH_ENDPOINT"]
  os.environ["LANGSMITH_PROJECT"] = LANGSMITH_SETTINGS["LANGSMITH_PROJECT"]


  # Initialize the database table for voices
  create_table()
  
  # Set the voice of the assistant
  Set_Voice(BUILD_SETTINGS["starterVoice"])
  
  # Initialize the assistant's visual component - Threaded to allow for concurrent execution
  if (DEV_SETTINGS["usingGUI"]):
    GUI_THREAD = threading.Thread(target=Init_Window)
    GUI_THREAD.start()
    GUI_THREAD.join(timeout=1)
    
  
  
  
  pass

