from tkinter import Menu

def init(root,**kwargs):
    # Menu bar
    menu = Menu(root)

    # cypher type items
    cyphermenu = Menu(menu, tearoff=0)
    cyphermenu.add_radiobutton(label="Concealment", command=kwargs['concealment_cyphers'])
    cyphermenu.add_radiobutton(label="Transposition", command=kwargs['transposition_cyphers'])
    cyphermenu.add_radiobutton(label="next cypher") # , command=donothing)
    menu.add_cascade(label="Cyphers", menu=cyphermenu)

    # mode menu items
    modemenu = Menu(menu, tearoff=0)
    modemenu.add_radiobutton(label="Decryption") # , command=donothing)
    modemenu.add_radiobutton(label="Encryption") # , command=donothing)
    menu.add_cascade(label="Mode", menu=modemenu)
    
    return menu