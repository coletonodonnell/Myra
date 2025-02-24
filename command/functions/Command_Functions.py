from response.RESPONSE import RESPONSE_SYSTEM
from execution.building.main_config import USER_NAME
from command.config import commandVariables


def Introduction():
	RESPONSE_SYSTEM.Custom_Response(f"Hello {USER_NAME}! How can I help you today?")
 
# Function that check if keyword to activate assistant is present in the query
def Check_For_Keyword(query, keyword):
    if keyword in query:
        return True
    else:
        return False


# Querying Functions ---------------------------------------------------------
# New Query Available Boolean Setter
def Set_New_Query_Available(value):
    global commandVariables
    commandVariables["newQueryAvailable"] = value
    return

# New Query Available Boolean Getter
def Is_New_Query_Available():
    global commandVariables
    return commandVariables["newQueryAvailable"]

# Current Query String Setter
def Set_Current_Query(value):
    global commandVariables
    commandVariables["currentQuery"] = value
    return

# Current Query String Getter
def Get_Current_Query():
    global commandVariables
    return commandVariables["currentQuery"]


# Command Functions ----------------------------------------------------------
# Change Activation Keyword Function
def Change_Activation_Keyword(new_keyword):
    global commandVariables
    commandVariables['activationKeyword'] = new_keyword
    print(f"Activation Keyword changed to: {commandVariables['activationKeyword']}")
    return

# Change Input Type Function
def Change_Input_Type(new_input_type):
    global commandVariables
    commandVariables["queryInputType"] = new_input_type
    print(f"Input Type Changed to: {commandVariables["queryInputType"]}")
    return commandVariables["queryInputType"]