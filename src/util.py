import re 

# removes everything but letters and numbers
def clean_message(message):
    return re.sub('[^\w]','', message)