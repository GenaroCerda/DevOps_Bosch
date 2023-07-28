import sys 

def greeting(lenguage) -> str:
    
    if lenguage=="English":
        msg="Hello World!"
    elif lenguage=="German":
        msg="Hallo Welt!"
    elif lenguage=="Spanish":
        msg="Hola Mundo!"
    elif lenguage=="Portuguese":
        msg="Olá mundo!"
    elif lenguage=="French":
        msg="Salut monde!"
    elif lenguage=="Italian":
        msg="Ciao mondo!"
    else:
        msg="Sorry that lenguage has not beed added yet"
        
    print(msg)
    return msg 
    
greeting(sys.argv[1])