import sys 

def greeting():

    lenguage=sys.argv[1]
    if lenguage=="English":
        msg="Hello World!"
    elif lenguage=="German":
        msg="Hallo Welt!"
    elif lenguage=="Spanish":
        msg="Hola Mundo!"
    elif lenguage=="Portuguese":
        msg="Olá mundo!"
    elif lenguage=="French":
        msg="Salut monde"
    elif lenguage=="Italian":
        msg="Ciao mondo"
    else:
        msg="Sorry that lenguage is not added yet to DB"
        
    print(msg)
    
greeting()