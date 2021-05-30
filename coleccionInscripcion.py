import numpy as np
import csv
from claseInscripcion import Inscripcion
class ColeccionInscripcion:
    __dimension=0
    __cantidad=0
    
    
    
    def __init__ (self,dimension=0):
        self.__inscripciones=np.empty(dimension,dtype=Inscripcion)
        self.__dimension=dimension
        self.__cantidad=0
        
    def agregarInscripcion (self, inscripcion):
        if self.__dimension==self.__cantidad:
            self.__dimension=self.__dimension+1
            self.__inscripciones.resize(self.__dimension)
        self.__inscripciones[self.__cantidad]=inscripcion
        self.__cantidad=self.__cantidad+1
        
        
    def mostrar (self):
        for inscripcion in self.__inscripciones:
            print(inscripcion)
        
        
        
        
    def buscarPersona (self):
        n=input("INGRESE NOMRE DE PERSONA QUE DEASEA BUSCAR")
        i=0
        inscripcion=self.__inscripciones[i]
        persona=inscripcion.getPersona()
        nom=persona.getNombre()
        long=self.__cantidad
        while(str(n)!=str(nom))and(int(i)<int(long)):
            i=i+1
            persona=self.__inscripciones[i].getPersona()
            nom=persona.getNombre()
            
        if i<long:
            return self.__inscripciones[i]
        
        else:
            return False
        
        
    def RegistrarPago (self):
        i=0
        dni=int(input("INGRESE EL DNI DE LA PERSONA\n"))
        ins=self.__inscripciones[i]
        per=ins.getPersona()
        d=int(per.getDni())
        lon=self.__cantidad
        while(int(dni)!=int(d))and(i<(int(lon))):
            ins=self.__inscripciones[i]
            per=ins.getPersona()
            d=int(per.getDni())
            i=i+1
        if i<lon:
            insc=self.__inscripciones[i]
            insc.setPago()
            print("SE REALIZO EL PAGO DE LA INSCRIPCION")
            print(insc.getPago())
        else:
            print("NO SE ENCONTRO A LA PERSONA")
            
            
    def GuardarIscriociones (self):
        
        archivo="inscripciones.csv"
        csv=open(archivo,"w")
        titulo="dniPersona,idTaller,fecha,pago\n"
        csv.write(titulo)
        for inscripcion in self.__inscripciones:
            p=inscripcion.getPersona()
            dni=p.getDni()
            t=inscripcion.getTaller()
            i=t.getId()
            f=inscripcion.getFecha()
            p=inscripcion.getPago()
            cad='{},{},{},{}\n'.format(dni,i,f,p)
            csv.write(cad)
        archivo.close()