from re import M
from tkinter import *

from cyphers import *
import util
import menu

# main window
root = Tk()
root.title('ez test')
concealment = Concealment(MODE.decrypt)
transposition = Transposition(MODE.decrypt)
substitution = Substitution(MODE.decrypt)

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

def substitution_cyphers():
    hide_widgets()
    key_entry.pack()
    substitution_caesar_button.pack()
    substitution_affine_button.pack()
    substitution_multiplicative_button.pack()

def encryption_mode():
    concealment.mode = MODE.encrypt
    transposition.mode = MODE.encrypt
    substitution.mode = MODE.encrypt

def decryption_mode():
    concealment.mode = MODE.decrypt
    transposition.mode = MODE.decrypt
    substitution.mode = MODE.decrypt

# concealment cypher buttons
bacon_button = Button(root, text='bacon',command=lambda: update_label('bacon'))
skip_button = Button(root, text='skip',command=lambda: update_label('skip'))
ladder_button = Button(root, text='ladder', command=lambda: update_label('ladder'))
reverse_button = Button(root, text='reverse', command=lambda: update_label('reverse'))

# transposition cyphers
transposition_number_button = Button(root, text='trans number', command=lambda: update_label('trans number'))
transposition_word_button = Button(root, text='trans word', command=lambda: update_label('trans word'))

# substitution cyphers
substitution_caesar_button = Button(root, text='caesar', command=lambda: update_label('caesar'))
substitution_multiplicative_button = Button(root, text='multiplicative', command=lambda: update_label('multiplicative'))
substitution_affine_button = Button(root, text='affine', command=lambda: update_label('affine'))


# Key entry
key_entry = Entry(root)

# all the widgets
widgets = [bacon_button, skip_button, ladder_button, reverse_button, key_entry, transposition_number_button, transposition_word_button, substitution_caesar_button, substitution_multiplicative_button, substitution_affine_button]


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
        message = concealment.bacon(util.clean_message(code_entry.get()))
    elif cypher == 'skip':
        message =  'skip every 1, start at 1: ' + concealment.skip(util.clean_message(code_entry.get()),2,0) + '\n'
        message += 'skip every 1, start at 2: ' + concealment.skip(util.clean_message(code_entry.get()),2,1) + '\n'
        message += 'skip every 2, start at 1: ' + concealment.skip(util.clean_message(code_entry.get()),3,0) + '\n'
        message += 'skip every 2, start at 2: ' + concealment.skip(util.clean_message(code_entry.get()),3,1) + '\n'
        message += 'skip every 2, start at 3: ' + concealment.skip(util.clean_message(code_entry.get()),3,2) + '\n'
        message += 'skip every 3, start at 1: ' + concealment.skip(util.clean_message(code_entry.get()),4,0) + '\n'
        message += 'skip every 3, start at 2: ' + concealment.skip(util.clean_message(code_entry.get()),4,1) + '\n'
        message += 'skip every 3, start at 3: ' + concealment.skip(util.clean_message(code_entry.get()),4,2) + '\n'
        message += 'skip every 3, start at 4: ' + concealment.skip(util.clean_message(code_entry.get()),4,3) + '\n'
        message += 'skip every 4, start at 1: ' + concealment.skip(util.clean_message(code_entry.get()),5,0) + '\n'
        message += 'skip every 4, start at 2: ' + concealment.skip(util.clean_message(code_entry.get()),5,1) + '\n'
        message += 'skip every 4, start at 3: ' + concealment.skip(util.clean_message(code_entry.get()),5,2) + '\n'
        message += 'skip every 4, start at 4: ' + concealment.skip(util.clean_message(code_entry.get()),5,3) + '\n'
        message += 'skip every 4, start at 5: ' + concealment.skip(util.clean_message(code_entry.get()),5,4) + '\n'


    elif cypher == 'ladder':
        message = concealment.ladder(util.clean_message(code_entry.get()))
    elif cypher == 'reverse':
        message = concealment.reverse(util.clean_message(code_entry.get()))
    elif cypher == 'trans number':
        message = transposition.trans_number(util.clean_message(code_entry.get()), key_entry.get())
    elif cypher == 'trans word':
        message = transposition.trans_word(util.clean_message(code_entry.get()), key_entry.get())
    elif cypher == 'caesar':
        message = substitution.caesar(util.clean_message(code_entry.get()), int(key_entry.get()))
    elif cypher == 'multiplicative':
        message = substitution.multiplicative(util.clean_message(code_entry.get()), int(key_entry.get()))
    elif cypher == 'affine':
        message = substitution.affine(util.clean_message(code_entry.get()), int(key_entry.get()))
    else:
        message = 'No Cypher was Selected'
    textbox.insert(END, message)

hide_widgets()

menubar = menu.init(root, concealment_cyphers=concealment_cyphers, transposition_cyphers=transposition_cyphers, substitution_cyphers=substitution_cyphers, decryption_mode=decryption_mode, encryption_mode=encryption_mode)
root.config(menu=menubar)
root.mainloop()