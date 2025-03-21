---
title: Proper Conventions
---
The proper conventions for the repo can found in this document. Please refer to any of the rules as needed and follow them accordingly when adding new functionality as close as you can.

## Naming Conventions

These are the proper naming conventions to be followed for files, folders, and anything else:

- **Folders:** all lower case (audio, command)
- **Configuration Files:** all lower case, must be named \*\_**config**.&nbsp;
  - To avoid confusion, do not put multiple config files in the same directory.
- **High-Level Files:** Full Capitalized, Single-word (ENTRY, TESTING).
  - HL Files are files which hold the most operational logic and use functional files to complete operations.&nbsp;
- **Functional Files:** Capitalized Snakecase (Response_Variation, Simple_Tasks).
  - Functional files contain functions that are used in operations by the assistant.&nbsp;
- **Miscellaneous Files:** Regular Snakecase ([build.py](http://build.py))
  - Any file that isn't a config, HL, or functional file.
- **Variables**
  - **Regular:** Camelcase (useSystemVoice, previousText)
  - **Static:** Full Capitalized Snakecase (ELEVENLABS_API_KEY)
- **Classes + Interfaces:** Pascalcase (TestBaselineSuite, Voice)
  - **Class Methods:** Camelcase (getName())
- **Functions:** Capitalized Snakecase (Set_Voice, Get_Query)
  - **Helper Functions:** Camelcase. Any logic functions not called outside of the file it's in.

## Commenting

Comments should be kept concise and small if embedded into code. If larger blocks of comments are needed, such as the beginning of the file or to explain a section of code, using dashes to separate a block of lines is preferred.

<SwmSnippet path="/command/QUERY.py" line="98">

---

Comment Section Separator

```python
        # Simple Requests ----------------------------------------------
        # Simple Requests are requests that are simple to execute that do not require 
        # any external API calls or complex logic. 
        # Examples include telling the time, opening a website, etc.
        #

        # # Tell Time
        # elif 'time' in query:
        #     Simple_Requests.tellTime()
        #     continue
                
        # Open Google
        elif "google" in query:
            Say("Opening Google.")
            Open_Websearch()
            continue
```

---

</SwmSnippet>

<SwmSnippet path="services/testing/TESTING.py" line="5">

---

Initial File Comment Block

```
# Testing Suite ---------------------------------------
# This is the high-level function that will run all testing functions.
# Testing functions should be split into files in separate directories.
# Configure the this file and testing files as neccesary.
# -----------------------------------------------------
```

---

</SwmSnippet>

## Folder Structure

Use your own discretion when creating folders to hold files. They should follow the naming convention and be intuitive to determine what the files inside of the folders do (for example, <SwmPath>[audio/](/audio/)</SwmPath> contains all audio related files).

&nbsp;

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
