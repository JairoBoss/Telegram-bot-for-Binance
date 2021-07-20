from datetime import datetime

def saludo(inputMessage):
    if (inputMessage in ("Hola","Hi",)):
        return "Que rollo"
    
    if (inputMessage in ("Adios","Bye",)):
        return "Amonos"
    
    return "No"
    