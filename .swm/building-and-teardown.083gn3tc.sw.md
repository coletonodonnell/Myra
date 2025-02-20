---
title: Building and Teardown
---
# Building

Myra needs to build specific classes and objects before she can run. The Build function takes care of this mainly. Any settings that need to be initialized or actions that need to be taken before Myra begins operating must start in the Build function.

Current Functions in <SwmToken path="/execution/building/build.py" pos="21:2:4" line-data="def Build():">`Build()`</SwmToken>:

- <SwmToken path="/audio/AUDIO.py" pos="159:2:2" line-data="def Set_Voice(voiceName):">`Set_Voice`</SwmToken>
- <SwmToken path="/video/VISUAL.py" pos="7:2:2" line-data="def Init_Window():">`Init_Window`</SwmToken>

<SwmSnippet path="/execution/building/build.py" line="21">

---

Current Build Function

```
def Build():

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
```

---

</SwmSnippet>

# Teardown

When the assistant shuts down, any lingering functions or methods must be taken care of in the <SwmToken path="/execution/teardown/teardown.py" pos="17:2:2" line-data="def Shutdown_Assistant(arg1, arg2):">`Shutdown_Assistant`</SwmToken> function. The first two arguments are to prevent an error from EEL GUI and are unused as of right now.

Current functions in <SwmToken path="/execution/teardown/teardown.py" pos="17:2:2" line-data="def Shutdown_Assistant(arg1, arg2):">`Shutdown_Assistant`</SwmToken>

- None

<SwmSnippet path="/execution/teardown/teardown.py" line="17">

---

Shutdown Function

```python
def Shutdown_Assistant(arg1, arg2):
    print("Shutting down the assistant...")
    
    
    # Forceful exit bc sys.exit() doesn't work with eel for some reason
    os._exit(0)
   
    pass
```

---

</SwmSnippet>

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
