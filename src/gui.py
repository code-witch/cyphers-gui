from tkinter import *

from cyphers import *
import util
import menu

# main window
root = Tk()
root.title('ez test')
concealment = Concealment(MODE.decrypt)
transposition = Transposition(MODE.decrypt)


def hide_widgets():
    for widget in widgets:
        widget.pack_forget() # remember to change to what ever style is being used... likely grid

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



# concealment cypher buttons
bacon_button = Button(root, text='bacon',command=lambda: update_label('bacon'))
skip_button = Button(root, text='skip',command=lambda: update_label('skip'))
ladder_button = Button(root, text='ladder', command=lambda: update_label('ladder'))
reverse_button = Button(root, text='reverse', command=lambda: update_label('reverse'))

# transposition cyphers
key_entry = Entry(root)
transposition_number_button = Button(root, text='trans number', command=lambda: update_label('trans number'))
transposition_word_button = Button(root, text='trans word', command=lambda: update_label('trans word'))

# all the widgets
widgets = [bacon_button, skip_button, ladder_button, reverse_button, key_entry, transposition_number_button, transposition_word_button]


# Message Entry
code_entry = Entry(root)
code_entry.pack()

# Text feedback
textbox = Text(root)
textbox.pack()

# GUI label update
def update_label(cypher):
    textbox.delete('1.0', END)
    message = ''
    if cypher == 'bacon':
        message = concealment.bacon('wOMB aNy nazi next aUSchwItz BurEaucraCY ENDED!')
    elif cypher == 'skip':
        message =  'skip every 1, start at 1: ' + concealment.skip('text here pls',2,0) + '\n'
        message += 'skip every 2, start at 1: ' + concealment.skip('text here pls',3,0) + '\n'
        message += 'skip every 1, start at 2: ' + concealment.skip('text here pls',2,1) + '\n'
        message += 'skip every 2, start at 2: ' + concealment.skip('text here pls',3,1) + '\n'
        message += 'skip every 2, start at 3: ' + concealment.skip('text here pls',3,2) + '\n'
        message += 'skip every 3, start at 1: ' + concealment.skip('text here pls',4,0) + '\n'
        message += 'skip every 3, start at 2: ' + concealment.skip('text here pls',4,1) + '\n'
        message += 'skip every 3, start at 3: ' + concealment.skip('text here pls',4,2) + '\n'
        message += 'skip every 3, start at 4: ' + concealment.skip('text here pls',4,3) + '\n'
        message += 'skip every 4, start at 1: ' + concealment.skip('text here pls',5,0) + '\n'
        message += 'skip every 4, start at 2: ' + concealment.skip('text here pls',5,1) + '\n'
        message += 'skip every 4, start at 3: ' + concealment.skip('text here pls',5,2) + '\n'
        message += 'skip every 4, start at 4: ' + concealment.skip('text here pls',5,3) + '\n'
        message += 'skip every 4, start at 5: ' + concealment.skip('text here pls',5,4) + '\n'

    elif cypher == 'ladder':
        message = concealment.ladder('text here pls')
    elif cypher == 'reverse':
        message = concealment.reverse('text here pls')
    elif cypher == 'trans number':
        message = trans_number(util.clean_message(), key_entry.get())
    elif cypher == 'trans word':
        message = trans_word(util.clean_message(), key_entry.get())
    else:
        message = 'No Cypher was Selected'
    textbox.insert(END, message)

hide_widgets()

menubar = menu.init(root, concealment_cyphers=concealment_cyphers, transposition_cyphers=transposition_cyphers)
root.config(menu=menubar)
root.mainloop()