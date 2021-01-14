import re 

# removes everything but letters and numbers
def clean_message():
    # fix this so it doesnt fuck up with wack characters
    message = ''
    # We dont need to use a file anymore will be removed in next major version
    # TODO: REMOVE
    # with open('data.txt', 'r') as f:
    #     message = f.read()
    return re.sub('[^\w]','', message)