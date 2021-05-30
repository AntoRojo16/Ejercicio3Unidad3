from claseManejadorTaller import ManejadorTaller
from coleccionPersona import ColeccionPersona
from coleccionInscripcion import ColeccionInscripcion
def test ():
    talleres=ManejadorTaller()
    talleres.testTaller()
    print("---SE MOSTRARAN LOS TALLERES----")
    talleres.mostrar()
    input()
    i=0
    personas=ColeccionPersona()
    inscripciones=ColeccionInscripcion()
    print("---CARGAR PERSONAS---")
    while(i==0):
        personas.agregarPersona(talleres,inscripciones)
        print("---SI DESEA SEGUIR CARGANDO PERSONAS INGRESE 0 DE LO CONTRARIO INGRESE 1---\n")
        i=int(input())
        print("i{}".format(i))
    print("---CONSULTAR TALLER----\n")
    talleres.consultarInscriptos()
    input()
    print("----REGISRAR PAGO----\n")
    inscripciones.RegistrarPago()
    input()
    print("----GUARADAR ARCHIVO----\n")
    inscripciones.GuardarIscriociones()

if __name__=="__main__":
    test()