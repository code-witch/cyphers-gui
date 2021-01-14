# removes everything but letters and numbers
def clean_message():
    # fix this so it doesnt fuck up with wack characters
    message = ''
    with open('data.txt', 'r') as f:
        message = f.read()
    return re.sub('[^\w]','', message)


# cyphers 
def bacon(message):
    alphabet = "abcdefghiklmnopqrstuwxyz"

    # split message into groups of 5
    message = [message[i:i+5] for i in range(0, len(message), 5)]

    # convert letters into 1's and 0's
    for i in range(0,len(message)):
        for j in range(0, len(message[i])):
            message[i] = list(message[i])
            if message[i][j].isupper():
                message[i][j] = '1'
            else: 
                message[i][j] = '0'
        message[i] = ''.join(message[i])

        # convert binary to decimal
        message[i] = int(message[i], 2)

        # convert to ascii
        try:
            message[i] = alphabet[message[i]]
        except:
            message[i] = '_' # if the cypher is broken fill with blank

    # smoosh together
    message = ''.join(message)
    # print(message)
    return message

def skip(message, amount, start):
    return message[start::amount]

def ladder(message):
    message = re.sub('[^\w\s+]','', message)
    message = re.sub(' ','\n', message)
    return ' '.join(message)

def reverse(message):
    return message[::-1]

# my cypher for kohler
# wOMB aNy nazi next aUSchwItz BurEaucraCY ENDED! 

def trans_number(message, key):
    return message

def trans_word(message, key):
    return message
