---
title: Response System
---
## Introduction

This doc gives a high level overview of the <SwmToken path="/response/types/ResponseClass.py" pos="9:2:2" line-data="class ResponseSystem:">`ResponseSystem`</SwmToken> It is located in <SwmPath>[response/](/response/)</SwmPath> under the <SwmPath>[response/RESPONSE.py](/response/RESPONSE.py)</SwmPath> file.

&nbsp;

## Response System

The <SwmToken path="/response/RESPONSE.py" pos="19:0:0" line-data="RESPONSE_SYSTEM = ResponseSystem(DEV_SETTINGS, BUILD_SETTINGS)">`RESPONSE_SYSTEM`</SwmToken> variable is instantiated in <SwmPath>[response/RESPONSE.py](/response/RESPONSE.py)</SwmPath> and acts as the main response system whenever the assistant needs to respond to something.&nbsp;

**IMPORTANT:** If you need the assistant to respond to something, import the <SwmToken path="/response/RESPONSE.py" pos="19:0:0" line-data="RESPONSE_SYSTEM = ResponseSystem(DEV_SETTINGS, BUILD_SETTINGS)">`RESPONSE_SYSTEM`</SwmToken> into your python file and call its available functions. Do not implement a new <SwmToken path="/response/types/ResponseClass.py" pos="9:2:2" line-data="class ResponseSystem:">`ResponseSystem`</SwmToken> class.

<SwmSnippet path="/response/RESPONSE.py" line="19">

---

Response System Variable

```python
RESPONSE_SYSTEM = ResponseSystem(DEV_SETTINGS, BUILD_SETTINGS)

```

---

</SwmSnippet>

&nbsp;

## Using the Response System

In order to use the <SwmToken path="/response/RESPONSE.py" pos="19:0:0" line-data="RESPONSE_SYSTEM = ResponseSystem(DEV_SETTINGS, BUILD_SETTINGS)">`RESPONSE_SYSTEM`</SwmToken>, you can simply call any of its methods depending on what you want the assistant to say. Some of the methods require additional parameters to specify how to respond to specifically to a broader category. Read the response functions section on how to use them.

&nbsp;

## Response Functions

---

### Custom Response

<SwmToken path="/response/functions/Custom_Respond.py" pos="5:2:2" line-data="def Custom_Response(text):">`Custom_Response`</SwmToken> is a method used to respond with any text string called in the method. If there isn't a descript method for what needs to be said, use this function.

Parameters:

- text: String, what you want the assistant to say.

<SwmSnippet path="/services/testing/responses/custom_response_suite.py" line="21">

---

Example

```python
        RESPONSE_SYSTEM_FOR_TESTING.Custom_Response("Hello World!")
```

---

</SwmSnippet>

&nbsp;

### Stall and Return from Stall

<SwmToken path="/response/functions/Stall.py" pos="15:2:2" line-data="def Stall():">`Stall`</SwmToken> and <SwmToken path="/response/functions/Return_From_Stall.py" pos="15:2:2" line-data="def Return_From_Stall():">`Return_From_Stall`</SwmToken> are methods used in conjunction to imitate verbal pauses. If an action needs to take time to complete, you can call these functions to make the assistant's response more human like.

Parameters:

- NONE

Current Stall and Return From Stall Response Variations:

- <SwmToken path="/response/functions/Stall.py" pos="6:0:0" line-data="STALLING_RESPONSES = [">`STALLING_RESPONSES`</SwmToken>
- <SwmToken path="/response/functions/Return_From_Stall.py" pos="6:0:0" line-data="RETURNING_RESPONSES = [">`RETURNING_RESPONSES`</SwmToken>

<SwmSnippet path="services/testing/responses/stall_suite.py" line="20">

---

Example

```
        RESPONSE_SYSTEM_FOR_TESTING.Stall()
        time.sleep(5)
        RESPONSE_SYSTEM_FOR_TESTING.Return_From_Stall()
```

---

</SwmSnippet>

&nbsp;

### Rejection

<SwmToken path="/response/types/ResponseClass.py" pos="33:3:3" line-data="    def Rejection(self, type):">`Rejection`</SwmToken> is a method that rejects the user. It encompasses every type and way you can reject a user and a possible reason behind it. It takes in a <SwmToken path="/response/types/ResponseClass.py" pos="39:2:2" line-data="class REJECTION_TYPES:">`REJECTION_TYPES`</SwmToken> rejection type already defined in the <SwmToken path="/response/RESPONSE.py" pos="19:0:0" line-data="RESPONSE_SYSTEM = ResponseSystem(DEV_SETTINGS, BUILD_SETTINGS)">`RESPONSE_SYSTEM`</SwmToken> class (no need to import) and gives the user a rejection based on the type needed.

Parameters:

- requestType: From <SwmToken path="/response/types/ResponseClass.py" pos="39:2:2" line-data="class REJECTION_TYPES:">`REJECTION_TYPES`</SwmToken>

Rejection Types

- QUESTION
- REQUEST
- ERROR

Current Rejection Variations:&nbsp;

- <SwmToken path="/response/functions/Rejection.py" pos="6:0:0" line-data="QUESTION_REJECTION_RESPONSES = [">`QUESTION_REJECTION_RESPONSES`</SwmToken>
- <SwmToken path="/response/functions/Rejection.py" pos="14:0:0" line-data="REQUEST_REJECTION_RESPONSES = [">`REQUEST_REJECTION_RESPONSES`</SwmToken>
- <SwmToken path="/response/functions/Rejection.py" pos="22:0:0" line-data="ERROR_REJECTION_RESPONSES = [">`ERROR_REJECTION_RESPONSES`</SwmToken>

<SwmSnippet path="services/testing/responses/rejection_suite.py" line="12">

---

Example

```
        RESPONSE_SYSTEM_FOR_TESTING.Rejection(RESPONSE_SYSTEM_FOR_TESTING.REJECTION_TYPES.QUESTION)
```

---

</SwmSnippet>

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="Myra"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
