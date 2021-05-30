from claseInscripcion import Inscripcion
class TallerCapacitacion:
    __idTaller=0
    __nombre=""
    __vacantes=0
    __montoInscripcion=0
    __inscripciones=[]
    
    
    def __init__(self,idT,nom,va,mon):
        self.__idTaller=idT
        self.__nombre=nom
        self.__vacantes=va
        self.__montoInscripcion=mon
        self.__inscripciones=[]
        
        
    def getId (self):
        return self.__idTaller
    
    
    def getNombre (self):
        return self.__nombre
    
    
    def getVacantes (self):
        return self.__vacantes
    
    def getInscripciones (self):
        return self.__inscripciones
    
    def getDimen (self):
        return len(self.__inscripciones)
    
    def getMonto (self):
        return self.__montoInscripcion
    
    
    def mostrarPersonasIns (self,i):
        print(self.__inscripciones[i].getPersona())
        
    
    def __str__ (self):
        i='ID del taller {}\n'.format(self.__idTaller)
        n='Nobre del taller {}\n'.format(self.__nombre)
        v='Cantidad de vacantes {}\n'.format(self.__vacantes)
        m='Monto de la inscripcion {}\n'.format(self.__montoInscripcion)
        cad=i+n+v+m
        return cad
    
    
    def setVacante (self):
        self.__vacantes=int(self.__vacantes)-1
        
        
    def setInscripcion (self,unaInscripcion):
        self.__inscripciones.append(unaInscripcion)        
         
    
    def get (self):
        i='ID del taller {}\n'.format(self.__idTaller)
        n='Nobre del taller {}\n'.format(self.__nombre)
        v='Cantidad de vacantes {}\n'.format(self.__vacantes)
        m='Monto de la inscripcion {}\n'.format(self.__montoInscripcion)
        cad=i+n+v+m
        return cad
        
    def mostrarInscripcion (self):
        for inscripcion in self.__inscripciones:
            print(inscripcion)