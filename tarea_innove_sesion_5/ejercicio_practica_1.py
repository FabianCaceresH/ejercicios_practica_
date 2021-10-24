# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con diccionarios

import csv
import os


def ej1():
    print('Ejercicios con diccionarios 1º')
    # Crear un diccionario vacio
    # el diccionario vacio debe llamarse "stock"
#hjadskhaodausadsdaiudidiuIDAIOQUNnn,mnfjkadsllaskjdhfasjdhfaksdjfhasudfysfasudgehqwgwqe

    stock = {'tornillos':100,'tuercas':150,'arandelas':200}

    # Luego de crear el diccionario completelo
    # con el siguiente stock:
    # tornillos = 100
    # tuercas = 150
    # arandelas = 300


    # Los nombres tornillos, tuercas y arandelas
    # son las claves (keys) del diccionario
    # mientras que las cantidades son los valores (values)

    # Una vez armado el diccionario imprimirlo en pantalla con print

    # Comenzar aquí, recuerde el identado dentro de esta funcion


def ej2():
    print('Ejercicio con diccionarios 2º')
    # Basado en el ejercicio anterior ej1, utilizaremos el diccionario
    # como una base de datos. Comenzaremos con un diccionario de stock
    # de nuestros productos en cero:
    
    stock = {'tornillos': 0, 'tuercas': 0, 'arandelas': 0}
while True:
    print("opcion 1: ingrese la cantidad de tornillos que decea")
    print("opcion 2: ingrese la cantidad de tuercas que decea")
    print("opcion 3: ingrese la cantidad de arandelas que decea")
    print("opcion 4:salir")
    producto = int(input("coloque  1,2 o 3 dependiendo de que decee"))
    if producto ==1:
        producto = stock['tornillos'] = int(input("ingrese la cantidad de tornillos que decee"))
        print(stock.items())
    if producto == 2:
        producto = stock['tuercas'] = int(input("ingrese la cantidad de tuercas que decee"))
        print(stock.items())
    if producto ==3: 
        producto = stock['tornillos'] = int(input("ingrese la cantidad de tornillos que decee"))
        print(stock.items())
    if producto == 4:
        print("terminó de ingresar los valores")
        print(f"el stock final es",{stock.items()})
        break
    else:
        print("coloque el numero de alguna de las opciones disponibles")
    # Paso 1:
    # Crear un bucle utilizando while que se ejecute de forma infinita
    # while True.....
    
    # Paso 2:
    # Dentro de ese bucle consultar al usuario por consola
    # que producto desea agregar al stock
    #   - Si el usuario ingresa "FIN" como producto se debe 
    #   finalizar el bucle
    #   - Si el usuario ingresa un producto no definido en el stock
    #   se debe enviar un mensaje de error. (si desea investigar esto
    #   se resuelve muy bien utilizando el operador "in" con diccionarios)

    # Paso 3:
    # Luego de haber ingresado el producto se debe ingresar por consola
    # cuanto stock de ese producto se desea agregar al stock.
    # Si teniamos 20 tornillos y el usuario desea agregar 10 tornillos más,
    # en nuestro diccionario deben quedar 30 tornillos (debe acumular)

    # Paso 4:
    # Cuando el usuario ingrese "FIN" y se termine el bucle, debe
    # imprimir en pantalla con print el diccionario con el stock final

    # Comenzar aquí, recuerde el identado dentro de esta funcion
def ej3():
    archivo = 'stock.csv'
    scv = open (archivo,'r')
    datos = list(csv.Dictreader(csv))
    columna = 'tornillos'
    cant_tornillos = 0
    for x in datos:
        data = x
        print("los tornillos por fila",data.get('tornillos'))
        cantidad = data.get('tornillos')
        if cantidad:
            cant_tornillos = cant_tornillos + int(cantidad)
        else:
            print("error en la ejecucion")
    print("la cantidad de tornillos en la columna es:",cant_tornillos)
    scv.close
def ej4():
    archico = propiedades.scv 
    lectura = open(archivo,'r')
    listado = list(csv.DictReader(lectura))
    cantidad_dep_2 = 0
    cantidad_dep_3 = 0
    for x in listado:
        dat =1
        print('ambientes:',dat.get('ambientes'))
        try:
            departamento = dat.get('ambientes')
            if int(departamento) == 2:
                cantidad_dep_2+= 1
            elif int(departamento) == 3:
                cantidad_dep_3 +=1
        except:
            continue
        print("La cantidad de departamentos de 2 ambientes es :", cantidad_dep_2)
        print("La cantidad de departamentos de 3 ambientes es :", cantidad_dep_3)
        lectura.close()
        if __name__ == '__main__':
            print("Bienvenidos a otra clase de Inove con Python")
            ej3()
            ej4()


 
