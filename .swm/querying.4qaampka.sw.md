---
title: Querying
---
## Introduction

This doc gives a high level overview of how querying works for Myra. The assistant's ability to take and recognize **commands** from the user operates from the main <SwmPath>[command/QUERY.py](/command/QUERY.py)</SwmPath> file.&nbsp;

## <SwmPath>[command/QUERY.py](/command/QUERY.py)</SwmPath>

The main functions of <SwmPath>[command/QUERY.py](/command/QUERY.py)</SwmPath> are:


- <SwmToken path="/command/QUERY.py" pos="15:2:4" line-data="def Introduction():">`Introduction()`</SwmToken>
- <SwmToken path="/command/QUERY.py" pos="19:2:4" line-data="def Get_Query():">`Get_Query()`</SwmToken>


## Design Decisions & Expansions

A singular function is used to determine queries for **Assistant Mode.** This SHOULD be changed for a better overall structure that will be interacting with other parts of the assistant. Please ensure you update this section if you are changing the main command structure.


## <SwmToken path="/command/QUERY.py" pos="19:2:4" line-data="def Get_Query():">`Get_Query()`</SwmToken>

This function is the **main query** **loop** for **Assistant Mode**. It starts with an <SwmToken path="/command/QUERY.py" pos="15:2:4" line-data="def Introduction():">`Introduction()`</SwmToken> and follows a while loop to take in a query from <SwmToken path="/audio/AUDIO.py" pos="17:2:2" line-data="def Take_Command():">`Take_Command`</SwmToken> and respond to the query accordingly based on audio or text input.


The current functionality of the function are:

- Return name of assistant
- Opening Google


<SwmSnippet path="command/QUERY.py" line="16">

---

Function Definition

```
	RESPONSE_SYSTEM.Custom_Response(f"Hello {USER_NAME}! How can I help you today?")
 

def Get_Query():
    
    Introduction()
    
    while(True):
        
        # Initialize the query ----------------------------------------
        # Input Channel Check - Audio or Text Box (TO DO)
        if queryInputType == "Audio":
            
            # Audio Keyword Check
            query = Take_Command().lower() # Take command from the user
            if Check_For_Keyword(query, activationKeyword) == False: # Check for the activation keyword
                print("Activation Keyword not found.")
                continue
            query = query.replace(activationKeyword, "") # Remove the activation keyword from the query
            
        elif queryInputType == "Text":
            print("Text Input is not supported yet.")
        else:
            print("Invalid Input Type.")
            break   
        
        if query == "NONE": continue
        print(f"User: {query}")
        
        
        
        # Execute the query -------------------------------------------
        
        # Exit Condition
        if 'never mind' in query: 
            RESPONSE_SYSTEM.Custom_Response("Goodbye!")
            Shutdown_Assistant()
            break
        
        # Question Parsing --------------------------------------------
        elif Question_Parse.Is_Question(query):
            
            
            # Identity 
            # TO DO: Consider all of the possible ways to ask for the name, account for variation
            if 'you' or 'your name' in query:
                RESPONSE_SYSTEM.Custom_Response(f"My name is Myra. Your personal assistant dummy!")
                continue
            
            
            # General Questions ---------------------------------------
            # 
            
            # Start GPT Response (NOT USED YET)
            '''
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-16k",
                messages=[
                    {"role": "system", "content": RESPONSE_SYSTEM_CONTEXT},
                    {"role": "user", "content": query}
                ]
            )
            
            
            # Get the response
            notResponded = True
            while (notResponded):
                if response.choices[0].message.content != None:
                    print(f'Myra: {response.choices[0].message.content}')
                    Say(response.choices[0].message.content)
                    notResponded = False
                else:
                    print('Waiting for response...')
            '''
            
            
            
            
            
            
            
                            
            continue
            

        
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
```

---

</SwmSnippet>


## <SwmToken path="/command/QUERY.py" pos="15:2:4" line-data="def Introduction():">`Introduction()`</SwmToken>

This is the introduction function used to introduce the assistant. It serves two purposes, to introduce Myra on startup and indicate that the user has switched from any other mode to **Assistant Mode**.

<SwmSnippet path="command/QUERY.py" line="15">


---

Function Definition

```
def Introduction():
	RESPONSE_SYSTEM.Custom_Response(f"Hello {USER_NAME}! How can I help you today?")
```

---

</SwmSnippet>

## 

## 

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
