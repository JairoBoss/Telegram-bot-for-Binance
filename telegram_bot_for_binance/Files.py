
class Controller:
    def __init__(self):
        pass

    def openFile(self):
        apis = []    
        try:
            file = open("Config/config.txt","r")
            for x in file:
                #print(x)
                apis.append(x)
            return apis
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
        return stringAux.strip()
    
                    
control = Controller()
