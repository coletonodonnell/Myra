---
title: Main Configuration
---
<SwmSnippet path="config/main_config.yaml" line="1">

---

Configuration Variables

```
User:
  Username: "Boss"
Keys:
  OPEN_AI_API_KEY: "KEY_HERE"
  ELEVENLABS_API_KEY: "KEY_HERE"
Voices:
  useSystemVoice: True
  starterVoice: "Taron"
  currentVoice: "Taron"
Development:
  devEnvironment: True
  usingGUI: True
  usingLLM: True
  usingOperations: True
  usingVoice: True

```

---

</SwmSnippet>

<SwmPath>[config/main_config.yaml](/config/main_config.yaml)</SwmPath> contains the main configuration variables for Myra including API keys, user variables and preferences, etc. They are read into the system at <SwmPath>[execution/building/main_config.py](/execution/building/main_config.py)</SwmPath> Depending on the variables filled out, some parts of the assistant may or may not work.&nbsp;&nbsp;&nbsp;

See <SwmPath>[config/main_config.yaml](/config/main_config.yaml)</SwmPath>and fill it out for development.

The current required keys are:

- Open AI API
- Elevenlabs (if using customizable voice)

## Future Expansions

For the Development section of the YAML file, there are several variables that can be True or False depending on what parts of the assistant you want to operate. Right now, only <SwmToken path="/config/main_config.yaml" pos="15:1:1" line-data="  usingVoice: True">`usingVoice`</SwmToken> and <SwmToken path="/config/main_config.yaml" pos="12:1:1" line-data="  usingGUI: True">`usingGUI`</SwmToken> function, as the rest of the systems aren't in place yet.

Once the Operations and LLM systems are operating correctly, they should be configured to be turned off and on with their respective variables for faster dev time.

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
