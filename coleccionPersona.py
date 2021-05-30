from clasePersona import Persona
from claseInscripcion import Inscripcion
import csv
class ColeccionPersona:
    
    
    def __init__ (self):
        self.__lista=[]
        
        
    def agregarPersona (self,talleres,inscripcion):
        nt=int(input("INGRESE NUMERO DEL TALLER A QUE DESEA INSCRIBIRSE \n"))
        t=talleres.buscarVacante(nt)
        if t:
            v=t.getVacantes()
            if int(v)>0:
                n=input("INGRESE  NOMBRE DE LA PERSONA \n")
                di=input("INGRESE LA DIRECCION \n")
                d=input("INGRESE EL DNI\n")
                unaPersona=Persona(n,di,d)
                self.__lista.append(unaPersona)
                t.setVacante()
                f=input("INGRESE FECHA\n")
                unaInscripcion=Inscripcion(f,unaPersona,t)
                inscripcion.agregarInscripcion(unaInscripcion)
                t.setInscripcion(unaInscripcion)
            else:
                print("NO ES POSIBLE HACER LA INSCRIPCION, LAS VACANTES SE ENCUENTRAN LLENAS")
                
        else:
            print("NO SE ENCOTRO EL TALLER INGRESADO")
                
        
    
    def mostrar  (self):
        for persona in self.__lista:
            print(persona)
        
    
