from command.config import queryInputType

# Changes the input type for the query
def Change_Input_Type(new_input_type):
    global queryInputType
    queryInputType = new_input_type
    print(f"Input Type Changed to: {new_input_type}")
    return queryInputType