from command.config import activationKeyword

# Function to change the activation keyword
def Change_Activation_Keyword(new_keyword):
    global activationKeyword
    activationKeyword = new_keyword
    print(f"Activation Keyword changed to: {new_keyword}")
    return