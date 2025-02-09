# Function that check if keyword to activate assistant is present in the query
def Check_For_Keyword(query, keyword):
    if keyword in query:
        return True
    else:
        return False
    