import csv
from os import close
def ej3():
    print('Ejercicio de archivos CSV 1º')
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo,
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    archivo = 'stock.csv'
    scv = open(archivo,'r')
    datos = list(csv.DictReader(csv))
    columna = 'tornillos'
    cant_tornillos = 0
    for x in datos:
        data = x
        print("Los tornillos por fila",data.get('tornillos'))
        cantidad = data.get('tornillos')
        if cantidad:
            cant_tornillos = cant_tornillos + int(cantidad)
        else:
            print("Error en la ejecucion")
    print("La cantidad de tornillos en la columan es :", cant_tornillos)
    scv.close()
def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    lectura = open(archivo, 'r')
    listado = list(csv.dictReader(lectura))
    cantidad_dep_2 = 0
    cantidad_dep_3 = 0
    for x in listado:
        dat =1
        print('ambientes: ', dat.get('ambientes'))
        try:
            departamento = dat.get('ambientes')
            if int(departamento) ==2:
                cantidad_dep_2 += 1
            elif int(departamento) == 3:
                cantidad_dep_3 += 1
        except:
            continue
    print("La cantidad de departamentos de 2 ambientes es :", cantidad_dep_2)
    print("La cantidad de departamentos de 3 ambientes es :", cantidad_dep_3)
    lectura.close()
if _name_ == '_main_':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()