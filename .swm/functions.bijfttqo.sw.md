---
title: Functions
---
## Introduction

This doc describes the functions of the <SwmPath>[command/](/command/)</SwmPath> folder and their associated usages. They can be found in <SwmPath>[command/functions/](/command/functions/)</SwmPath> in the all-in-one file <SwmPath>[command/functions/Command_Functions.py](/command/functions/Command_Functions.py)</SwmPath>

## List of Functions

- <SwmToken path="/command/functions/Command_Functions.py" pos="43:2:2" line-data="def Change_Activation_Keyword(new_keyword):">`Change_Activation_Keyword`</SwmToken>
- <SwmToken path="/command/functions/Command_Functions.py" pos="50:2:2" line-data="def Change_Input_Type(new_input_type):">`Change_Input_Type`</SwmToken>
- <SwmToken path="/command/functions/Command_Functions.py" pos="10:2:2" line-data="def Check_For_Keyword(query, keyword):">`Check_For_Keyword`</SwmToken>
- <SwmToken path="/command/functions/Command_Functions.py" pos="19:2:2" line-data="def Set_New_Query_Available(value):">`Set_New_Query_Available`</SwmToken>
- <SwmToken path="/command/functions/Command_Functions.py" pos="25:2:2" line-data="def Is_New_Query_Available():">`Is_New_Query_Available`</SwmToken>
- <SwmToken path="/command/functions/Command_Functions.py" pos="30:2:2" line-data="def Set_Current_Query(value):">`Set_Current_Query`</SwmToken>
- <SwmToken path="/command/functions/Command_Functions.py" pos="36:2:2" line-data="def Get_Current_Query():">`Get_Current_Query`</SwmToken>
- <SwmToken path="/command/functions/Command_Functions.py" pos="6:2:2" line-data="def Introduction():">`Introduction`</SwmToken>

---

&nbsp;

### <SwmToken path="/command/functions/Command_Functions.py" pos="43:2:2" line-data="def Change_Activation_Keyword(new_keyword):">`Change_Activation_Keyword`</SwmToken>

- Changes the activation keyword in the <SwmPath>[command/config.py](/command/config.py)</SwmPath>. It is currently set to Myra, the assistant's name on startup.

### <SwmToken path="/command/functions/Command_Functions.py" pos="50:2:2" line-data="def Change_Input_Type(new_input_type):">`Change_Input_Type`</SwmToken>

- Changes the query input type in the <SwmPath>[command/config.py](/command/config.py)</SwmPath>. There are two options available: Audio or Text.

### <SwmToken path="/command/functions/Command_Functions.py" pos="10:2:2" line-data="def Check_For_Keyword(query, keyword):">`Check_For_Keyword`</SwmToken>

- Helper function that checks for the keyword activation.

### <SwmToken path="/command/functions/Command_Functions.py" pos="19:2:2" line-data="def Set_New_Query_Available(value):">`Set_New_Query_Available`</SwmToken>

- Parameters:
  - value: boolean
- Sets <SwmToken path="/command/functions/Command_Functions.py" pos="21:4:4" line-data="    commandVariables[&quot;newQueryAvailable&quot;] = value">`newQueryAvailable`</SwmToken> flag to the parameter value.

### <SwmToken path="/command/functions/Command_Functions.py" pos="25:2:2" line-data="def Is_New_Query_Available():">`Is_New_Query_Available`</SwmToken>

- Returns <SwmToken path="/command/functions/Command_Functions.py" pos="21:4:4" line-data="    commandVariables[&quot;newQueryAvailable&quot;] = value">`newQueryAvailable`</SwmToken>.

### <SwmToken path="/command/functions/Command_Functions.py" pos="30:2:2" line-data="def Set_Current_Query(value):">`Set_Current_Query`</SwmToken>

- Parameters:
  - query: String
- Sets <SwmToken path="/command/functions/Command_Functions.py" pos="32:4:4" line-data="    commandVariables[&quot;currentQuery&quot;] = value">`currentQuery`</SwmToken> string to parameter value.

### <SwmToken path="/command/functions/Command_Functions.py" pos="36:2:2" line-data="def Get_Current_Query():">`Get_Current_Query`</SwmToken>

- Returns <SwmToken path="/command/functions/Command_Functions.py" pos="32:4:4" line-data="    commandVariables[&quot;currentQuery&quot;] = value">`currentQuery`</SwmToken>.

### <SwmToken path="/command/functions/Command_Functions.py" pos="6:2:2" line-data="def Introduction():">`Introduction`</SwmToken>

- Calls the <SwmToken path="/response/RESPONSE.py" pos="19:0:0" line-data="RESPONSE_SYSTEM = ResponseSystem(DEV_SETTINGS, BUILD_SETTINGS)">`RESPONSE_SYSTEM`</SwmToken> to introduce Myra. Serves two purposes, to introduce the assistant and indicate that Myra has switched into assistant mode.

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="Myra"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
