from command.config import *
from audio.AUDIO import *
from command.functions.Command_Functions import Check_For_Keyword, Set_Current_Query

def Is_New_Query():
    global commandVariables
    
    # Evaluate Query Input Type
    query = ""
    
    if commandVariables['queryInputType'] == "Audio":
            
        # Audio Keyword Check
        query = Take_Command().lower() # Take command from the user
        if Check_For_Keyword(query, commandVariables['activationKeyword']) == False: # Check for the activation keyword
            print("Activation Keyword not found.")
            return "NONE"
        query = query.replace(commandVariables['activationKeyword'], "") # Remove the activation keyword from the query
        Set_Current_Query(query) # Set the current query as a variable
        
            
    elif commandVariables['queryInputType'] == "Text":
        # Check if new query is available
        if commandVariables['newQueryAvailable'] == False: return "NONE"
        
        query = commandVariables['currentQuery']
    else:
        print("Invalid Input Type.")
    
    
    # Print the query
    print(f"User: {query}")
    
    # Set New Query to False
    commandVariables['newQueryAvailable'] = False
    
    # Return Query
    return query