class Inscripcion:
    __fechaInscripcion=0
    __pago=False
    __Taller=None
    __Persona=None
    
    
    
    
    def __init__ (self,f,persona,taller,p=False):
        self.__fecha=f
        self.__pago=p
        self.__Persona=persona
        self.__Taller=taller
        
        
    
    def getPersona (self):
        return self.__Persona
    
    def getFecha  (self):
        return self.__fecha
    
    def getTaller (self):
        return self.__Taller
    
    def getPago (self):
        return self.__pago
    
    def setPago (self):
        self.__pago=True
    
    def __str__ (self):
        f='Inscripcio {}\n'.format(self.__fecha)
        p='Pago del taller {}\n'.format(self.__pago)
        per=self.__Persona.get()
        ta=self.__Taller.get()
        return f+p+per+ta
        
    
    
    

