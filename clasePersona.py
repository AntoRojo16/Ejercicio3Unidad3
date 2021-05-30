class Persona:
    __nombre=""
    __direccion=""
    __dni=0
    
    
    def __init__ (self,nom,di,dni):
        self.__nombre=nom
        self.__direccion=di
        self.__dni=dni
        
        
        
    def getNombre(self):
        return self.__nombre
    
    
    def getdireccion (self):
        return self.__direccion
    
    
    
    def getDni (self):
        return self.__dni
    
    
    def get (self):
        n='Nombre {}\n'.format(self.__nombre)
        d='Direccion {}\n'.format(self.__direccion)
        dni='DNI {}\n'.format(self.__dni)
        return n+d+dni
    
    
    def __str__ (self):
        n='Nombre {}\n'.format(self.__nombre)
        d='Direccion{}\n'.format(self.__direccion)
        dni='DNI {}\n'.format(self.__dni)
        return n+d+dni
    
    
    
