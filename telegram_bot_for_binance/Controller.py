class Controller:
    def __init__(self):
        pass        

    def openFile(self):        
        try:
            file = open("Config/config.txt","r")
            for x in file:
                print(x)
            print(type(file))
        except OSError as e:
            print('Error! '+ str(e))
        finally:
            file.close()

    def getKey(self,userKey):
        aux = False
        stringAux = ""
        for x in userKey:
            if (x == "'" or aux == True):
                aux = True
                if(x == "'"):
                    continue
        #        print(x, end="")
                stringAux += x
        return stringAux
    
    
control = Controller()
#control.openFile()
a = "API_KEY_TELEGRAM = 'AAA'"
print(control.getKey(a))