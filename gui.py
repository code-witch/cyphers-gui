from tkinter import *
import re 

from cyphers import *

# main window
root = Tk()
root.title('ez test')

# concealment cypher buttons
bacon_button = Button(root, text='bacon',command=lambda: update_label('bacon'))
skip_button = Button(root, text='skip',command=lambda: update_label('skip'))
ladder_button = Button(root, text='ladder', command=lambda: update_label('ladder'))
reverse_button = Button(root, text='reverse', command=lambda: update_label('reverse'))

#transposition cyphers
key_entry = Entry(root)
transposition_number_button = Button(root, text='trans number', command=lambda: update_label('trans number'))
transposition_word_button = Button(root, text='trans word', command=lambda: update_label('trans word'))


# placing buttons

# bacon_button.pack()
# skip_button.pack()
# ladder_button.pack()
# reverse_button.pack()

key_entry.pack()
transposition_number_button.pack()
transposition_word_button.pack()


# label feedback
textbox = Text(root)
textbox.pack()

# GUI label update
def update_label(cypher):
    textbox.delete('1.0', END)
    message = ''
    if cypher == 'bacon':
        message = bacon(clean_message())
    elif cypher == 'skip':
        message =  'skip every 1, start at 1: ' + skip(clean_message(),2,0) + '\n'
        message += 'skip every 1, start at 2: ' + skip(clean_message(),2,1) + '\n'
        message += 'skip every 2, start at 1: ' + skip(clean_message(),3,0) + '\n'
        message += 'skip every 2, start at 2: ' + skip(clean_message(),3,1) + '\n'
        message += 'skip every 2, start at 3: ' + skip(clean_message(),3,2) + '\n'
        message += 'skip every 3, start at 1: ' + skip(clean_message(),4,0) + '\n'
        message += 'skip every 3, start at 2: ' + skip(clean_message(),4,1) + '\n'
        message += 'skip every 3, start at 3: ' + skip(clean_message(),4,2) + '\n'
        message += 'skip every 3, start at 4: ' + skip(clean_message(),4,3) + '\n'
        message += 'skip every 4, start at 1: ' + skip(clean_message(),5,0) + '\n'
        message += 'skip every 4, start at 2: ' + skip(clean_message(),5,1) + '\n'
        message += 'skip every 4, start at 3: ' + skip(clean_message(),5,2) + '\n'
        message += 'skip every 4, start at 4: ' + skip(clean_message(),5,3) + '\n'
        message += 'skip every 4, start at 5: ' + skip(clean_message(),5,4) + '\n'

    elif cypher == 'ladder':
        with open('data.txt', 'r') as f:
            message = ladder(f.read())
    elif cypher == 'reverse':
        message = reverse(clean_message())
    elif cypher == 'trans number':
        message = trans_number(clean_message(), key_entry.get())
    elif cypher == 'trans word':
        message = trans_word(clean_message(), key_entry.get())
    else:
        message = 'No Cypher was Selected'
    textbox.insert(END, message)

# removes everything but letters and numbers
def clean_message():
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

root.mainloop()