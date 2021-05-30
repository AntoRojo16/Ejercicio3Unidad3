import numpy as np
import csv
from claseTallerCapacitacion import TallerCapacitacion
from claseInscripcion import Inscripcion
from clasePersona import Persona
class ManejadorTaller:
    __dimencion=0
    __cantidad=0
    
    
    def __init__ (self,dimencion=0):
        self.__talleres=np.empty(dimencion,dtype=TallerCapacitacion)
        self.__dimencion=dimencion
        self.__cantidad=0
     
        
    def agregarTaller (self, unTaller,cantidad):
        self.__talleres[cantidad]=unTaller
        
    def testTaller (self):
        archivo=open("Talleres.csv")
        reader=csv.reader(archivo,delimiter=";")
        band=True
        for fila in reader:
            if band:
                dimension=fila[0]
                self.__talleres.resize(int(dimension))
                band=not  band    
            else:
                i=fila[0]
                n=fila[1]
                v=fila[2] 
                m=fila[3]
                unTaller=TallerCapacitacion(i,n,v,m)
                self.agregarTaller(unTaller,self.__cantidad)
                self.__cantidad=self.__cantidad+1
                
        archivo.close()
                
                
    def mostrar (self):
        for taller in self.__talleres:
            print(taller)
        
        
    def buscarVacante (self,n):
        
        i=0
        unTaller=self.__talleres[i]
        num=int(unTaller.getId())
        di=int(self.__cantidad)
        while(i<di)and(int(n)!=int(num)):
            unTaller=self.__talleres[i]
            num=unTaller.getId()
            i=i+1
        if i<di:
            return self.__talleres[i]
        
        else:
            return False
        
        
    def consultarInscriptos (self):
        n=input("INGRESE ID DEL TALLER\n")
        t=self.buscarVacante(n)
        if t!=False:
            dim=t.getDimen()
            if dim!=0:
                print("SE MOSTRARAN LAS PERSONAS INSCRIPTAS\n")
                for i in range(dim):
                    t.mostrarPersonasIns(i)
            else:
                print("El taller ingresado aun no cuenta con inscripciones")
        else:
            print("EL TALLER INGRESADO ES INCORRECTO")
        
        
    
        
        
    
        
    
