---
title: Querying
---
## Introduction

This doc gives a high level overview of how querying works for Myra. The assistant's ability to take and recognize **commands** from the user operates from the main <SwmPath>[command/QUERY.py](/command/QUERY.py)</SwmPath> file.&nbsp;

## <SwmPath>[command/QUERY.py](/command/QUERY.py)</SwmPath>

The main functions of <SwmPath>[command/QUERY.py](/command/QUERY.py)</SwmPath> are:

- <SwmToken path="/command/QUERY.py" pos="20:1:3" line-data="    Introduction()">`Introduction()`</SwmToken>
- <SwmToken path="/command/QUERY.py" pos="18:2:2" line-data="def Main_Query_Loop():">`Main_Query_Loop`</SwmToken>
- <SwmToken path="/command/QUERY.py" pos="25:5:7" line-data="        query = Is_New_Query()">`Is_New_Query()`</SwmToken>
- Core_Process()

## Design Decisions & Expansions

A singular function is used to determine queries for **Assistant Mode.** This SHOULD be changed for a better overall structure that will be interacting with other parts of the assistant. Please ensure you update this section if you are changing the main command structure.

## <SwmToken path="/command/QUERY.py" pos="18:2:2" line-data="def Main_Query_Loop():">`Main_Query_Loop`</SwmToken>

This function is the **main query** **loop** for **Assistant Mode**. It starts with an <SwmToken path="/command/QUERY.py" pos="20:1:3" line-data="    Introduction()">`Introduction()`</SwmToken> and follows a while loop to take in a query from <SwmToken path="/command/QUERY.py" pos="25:5:7" line-data="        query = Is_New_Query()">`Is_New_Query()`</SwmToken> and sends the query to the Core_Process() .

The current functionality of the function are:

- Return name of assistant
- Opening Google

<SwmSnippet path="/command/QUERY.py" line="18">

---

Function Definition

```
def Main_Query_Loop():
    
    Introduction()
    
    while(True):
        
        # Check if new query is available
        query = Is_New_Query()
        if query == "NONE": continue

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
        
        # Run Core Processor?
        Core_Process(query)
        
        
        
        # Execute the query -------------------------------------------
        
        
        
       
            
            # General Questions ---------------------------------------
            # 
            
            # Start GPT Response (NOT USED YET)
            # '''
            # response = client.chat.completions.create(
            #     model="gpt-3.5-turbo-16k",
            #     messages=[
            #         {"role": "system", "content": RESPONSE_SYSTEM_CONTEXT},
            #         {"role": "user", "content": query}
            #     ]
            # )
            
            
            # # Get the response
            # notResponded = True
            # while (notResponded):
            #     if response.choices[0].message.content != None:
            #         print(f'Myra: {response.choices[0].message.content}')
            #         Say(response.choices[0].message.content)
            #         notResponded = False
            #     else:
            #         print('Waiting for response...')
            # '''
            

        
        
```

---

</SwmSnippet>

## 

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBUENBQSUzQSUzQUF2YWxvbkFjZQ==" repo-name="PCAA"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
