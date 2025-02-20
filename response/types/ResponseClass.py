from execution.building.main_config import ELEVENLABS_API_KEY, BUILD_SETTINGS, DEV_SETTINGS

# Functions
from response.functions.Custom_Respond import Custom_Response
from response.functions.Stall import Stall
from response.functions.Return_From_Stall import Return_From_Stall
from response.functions.Rejection import Rejection


class ResponseSystem:
    def __init__(self, dev_settings, build_settings):
        self.dev_settings = dev_settings
        self.build_settings = build_settings
        
        # Rejection Types
        self.REJECTION_TYPES = REJECTION_TYPES
        
        # Conversational Mode
        self.Conversational_Mode = False
        
        pass
    
    # Response Functions ------------------------------------------------------
    # def Evaluate_For_Response(self, responseType, response, isReprompt = False, REJECTION_TYPE = None):
    #     # If the response is a reprompt, then call bypass of new query
    #     # if isReprompt: return
    #     # TO DO: Implement this
        
    #     # Call the response function based on the response type
    #     if responseType == "Custom":
    #         self.Custom_Response(response)
    #     elif responseType == "Stall":
    #         self.Stall()
    #     elif responseType == "Return":
    #         self.Return_From_Stall()
    #     elif responseType == "Rejection":
    #         if REJECTION_TYPE == "Question":
    #             self.Rejection(self.REJECTION_TYPES.QUESTION) # Rejection Type is required
    #         elif REJECTION_TYPE == "Request":
    #             self.Rejection(self.REJECTION_TYPES.REQUEST)
    #     else: 
    #         print("Invalid Response Type found in response system.")
    #     pass
    
    def Custom_Response(self, text):
        # Say the text with no parameters for now.
        Custom_Response(text)
        
    def Stall(self):
        # Stall the response system
        Stall()
        pass
    
    def Return_From_Stall(self):
        # Return from the stall
        Return_From_Stall()
        pass
    
    def Rejection(self, type):
        # Reject the request
        Rejection(type)
        pass
    
    
    
    # Conversational Functions ------------------------------------------------
    def Leave_Conversation(self):
        self.Conversational_Mode = False
        pass
    
    def Enter_Conversation(self):
        self.Conversational_Mode = True
        pass
    
    def Is_In_Conversational_Mode(self):
        return self.Conversational_Mode
    

    
class REJECTION_TYPES:
    QUESTION = "Question"
    REQUEST = "Request"
    ERROR = "Error"
    pass