from audio.AUDIO import Say

import random

# Question rejection responses
QUESTION_REJECTION_RESPONSES = [
    "I'm sorry, I can't answer that.",
    "I'm not sure... Sorry!",
    "I... really don't know the answer to that.",
    "That question is a bit too complex for me to answer, sorry.",
]

# Request rejection responses
REQUEST_REJECTION_RESPONSES = [
    "I'm sorry, I don't think I can do that.",
    "Well, that is something beyond my capabilities. So... no.",
    "Hmm... That is something I can't do.",
    "I don't think I can do that, sorry.",
]

# Error rejection responses
ERROR_REJECTION_RESPONSES = [
    "I'm sorry, I encountered an error. You might want to ask me again.",
    "Something went wrong while trying to do what you asked. Maybe ask me again?",
    "I'm sorry, I don't think I can do that right now. Something went wrong.",
    "Hmm... Seems I'm running into some issues right now. Sorry about that.",
]
    

# Rejection response for the system
def Rejection(requestType):
    
    match requestType:
        case "Question":
            Say(random.choice(QUESTION_REJECTION_RESPONSES))
        case "Request":
            Say(random.choice(REQUEST_REJECTION_RESPONSES))
        case "Error":
            Say(random.choice(ERROR_REJECTION_RESPONSES))
        case _:
            print("Invalid rejection type for response system. Please check the type.")
    
    pass