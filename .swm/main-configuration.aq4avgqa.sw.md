---
title: Main Configuration
---

<SwmSnippet path="main_config.py" line="3">

---

Configuration Variables

```
# Load the configuration for main
with open("./config/main_config.yaml", "r") as file:
  main_config = yaml.safe_load(file)

# Load Variables
OPEN_AI_API_KEY = main_config["Keys"]["OPEN_AI_API_KEY"]
ELEVENLABS_API_KEY = main_config["Keys"]["ELEVENLABS_API_KEY"]
USER_NAME = main_config["User"]["Username"]

BUILD_SETTINGS = {
  "systemVoice" : main_config["Voices"]["useSystemVoice"],
  "starterVoice": main_config["Voices"]["starterVoice"],
  "currentVoice": main_config["Voices"]["currentVoice"],
}
```

---

</SwmSnippet>

<SwmPath>[main_config.py](/main_config.py)</SwmPath> contains the main configuration variables for Myra including API keys, user variables and preferences, etc. All API keys must be filled with a usable API key for certain parts of the assistant to work.&nbsp;&nbsp;

See <SwmPath>[config/main_config.yaml](/config/main_config.yaml)</SwmPath>and fill it out for development.

The current required keys are:

- Open AI API
- Elevenlabs (if using customizable voice)

## Future Expansions

The configuration currently is a YAML file that is read and loaded into variables for the system to use. This should be changed to a personal database which can be saved and opened. For now this works, but make sure you don't commit your <SwmPath>[config/main_config.yaml](/config/main_config.yaml)</SwmPath> to the repo.

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
