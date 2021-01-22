def capturar ():
    global lista
    lista=[]
    print ("¿Cuantos elementos almacenará la lista?")
    n=input()
    n=int (n)
    for i in range (0, n):
        print ("Ingrese elemento para el índice: ", i)
        elemento=input()
        lista.insert (i, elemento)
def mostrar():
    print (lista)

def agregar():
   print ("Ingresa el elemento que desea agregar: ")
   elemento=input ()
   print ("Ingresa el índice donde desea agregarlo: ")
   indice=input()
   indice=int (indice)
   longitud=len(lista)
   longitud=int(longitud)
   if (indice>longitud or indice<0):
       print ("El índice debe estar entre 0 y ", longitud)
   else:
       lista.insert(indice, elemento)
       print ("Elemento agregado: ")
def eliminar():
    print("Ingresa el índice del elemento a eliminar: ")
    indice = input()
    indice = int(indice)
    longitud = len(lista)
    longitud = int(longitud)
    if (indice > longitud or indice < 0):
        print("El índice debe estar entre 0 y ", longitud-1)
    else:
        del lista[indice]
        print("Elemento agregado: ")
def modificar():
    print("Ingresa el índice del elemento a modificar : ")
    indice = input()
    indice = int(indice)
    print ("Ingrese el nuevo elemento: ")
    elemento=input()
    longitud = len(lista)
    longitud = int(longitud)
    if (indice > longitud or indice < 0):
        print("El índice debe estar entre 0 y ", longitud-1)
    else:
        lista[indice]=elemento
        print("Elemento modificado: ")
def menú():
    opcion="1"
    while(opcion!="6"):
        print ("Operaciones sobre la lista")
        print("1. Capturar nuevos elementos")
        print("2. Mostrar lista")
        print("3. Agregar un elemento a la lista")
        print("4. Eliminar un elemento de la lista")
        print("5. Modificar un elemento de la lista")
        print("6. Salir")
        print("Eliga una opción")
        opcion=input()
        if (opcion=="1"):
            capturar()
        elif (opcion=="2"):
            mostrar()
        elif (opcion == "3"):
            agregar()
        elif (opcion == "4"):
            eliminar()
        elif (opcion == "5"):
            modificar()
        elif (opcion == "6"):
            print ("Finalizado")
        else:
            print ("La opción que eligió no existe")
menú()
