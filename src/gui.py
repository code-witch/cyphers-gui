from tkinter import *

from cyphers import *
import util

# main window
root = Tk()
root.title('ez test')

def hide_widgets():
    for widget in widgets:
        widget.pack_forget()

def concealment_cyphers():
    hide_widgets()
    bacon_button.pack()
    skip_button.pack()
    ladder_button.pack()
    reverse_button.pack()


def transposition_cyphers():
    hide_widgets()
    key_entry.pack()
    transposition_number_button.pack()
    transposition_word_button.pack()

# Menu bar
menu = Menu(root)

# cypher type items
cyphermenu = Menu(menu, tearoff=0)
cyphermenu.add_radiobutton(label="Concealment", command=concealment_cyphers)
cyphermenu.add_radiobutton(label="Transposition", command=transposition_cyphers)
cyphermenu.add_radiobutton(label="next cypher") # , command=donothing)
menu.add_cascade(label="Cyphers", menu=cyphermenu)

# mode menu items
modemenu = Menu(menu, tearoff=0)
modemenu.add_radiobutton(label="Decryption") # , command=donothing)
modemenu.add_radiobutton(label="Encryption") # , command=donothing)
menu.add_cascade(label="Mode", menu=modemenu)


# concealment cypher buttons
bacon_button = Button(root, text='bacon',command=lambda: update_label('bacon'))
skip_button = Button(root, text='skip',command=lambda: update_label('skip'))
ladder_button = Button(root, text='ladder', command=lambda: update_label('ladder'))
reverse_button = Button(root, text='reverse', command=lambda: update_label('reverse'))

#transposition cyphers
key_entry = Entry(root)
transposition_number_button = Button(root, text='trans number', command=lambda: update_label('trans number'))
transposition_word_button = Button(root, text='trans word', command=lambda: update_label('trans word'))

widgets = [bacon_button, skip_button, ladder_button, reverse_button, key_entry, transposition_number_button, transposition_word_button]


# label feedback
textbox = Text(root)
textbox.pack()

# GUI label update
def update_label(cypher):
    textbox.delete('1.0', END)
    message = ''
    if cypher == 'bacon':
        message = bacon(util.clean_message())
    elif cypher == 'skip':
        message =  'skip every 1, start at 1: ' + skip(util.clean_message(),2,0) + '\n'
        message += 'skip every 1, start at 2: ' + skip(util.clean_message(),2,1) + '\n'
        message += 'skip every 2, start at 1: ' + skip(util.clean_message(),3,0) + '\n'
        message += 'skip every 2, start at 2: ' + skip(util.clean_message(),3,1) + '\n'
        message += 'skip every 2, start at 3: ' + skip(util.clean_message(),3,2) + '\n'
        message += 'skip every 3, start at 1: ' + skip(util.clean_message(),4,0) + '\n'
        message += 'skip every 3, start at 2: ' + skip(util.clean_message(),4,1) + '\n'
        message += 'skip every 3, start at 3: ' + skip(util.clean_message(),4,2) + '\n'
        message += 'skip every 3, start at 4: ' + skip(util.clean_message(),4,3) + '\n'
        message += 'skip every 4, start at 1: ' + skip(util.clean_message(),5,0) + '\n'
        message += 'skip every 4, start at 2: ' + skip(util.clean_message(),5,1) + '\n'
        message += 'skip every 4, start at 3: ' + skip(util.clean_message(),5,2) + '\n'
        message += 'skip every 4, start at 4: ' + skip(util.clean_message(),5,3) + '\n'
        message += 'skip every 4, start at 5: ' + skip(util.clean_message(),5,4) + '\n'

    elif cypher == 'ladder':
        with open('data.txt', 'r') as f:
            message = ladder(f.read())
    elif cypher == 'reverse':
        message = reverse(util.clean_message())
    elif cypher == 'trans number':
        message = trans_number(util.clean_message(), key_entry.get())
    elif cypher == 'trans word':
        message = trans_word(util.clean_message(), key_entry.get())
    else:
        message = 'No Cypher was Selected'
    textbox.insert(END, message)

hide_widgets()
root.config(menu=menu)
root.mainloop()