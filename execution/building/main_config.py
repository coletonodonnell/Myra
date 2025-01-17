import yaml

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

DEV_SETTINGS = {
  "isDevEnv"    : main_config["Development"]["devEnvironment"],
  "usingGUI"    : main_config["Development"]["usingGUI"],
  "usingVoice"  : main_config["Development"]["usingVoice"],
  "usingLLM"    : main_config["Development"]["usingLLM"],
  "usingOperations" : main_config["Development"]["usingOperations"],
}