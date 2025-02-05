
import speech_recognition as sr

from response.RESPONSE import RESPONSE_SYSTEM
from audio.AUDIO import *
from command.Simple_Requests import *
from interpretation.assistant import Question_Parse


from execution.building.main_config import USER_NAME
from execution.teardown.teardown import *
from command.config import *
from command.functions.Check_For_Keyword import Check_For_Keyword

def Introduction():
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
        elif "google" in query:
            Say("Opening Google.")
            Open_Websearch()
            continue