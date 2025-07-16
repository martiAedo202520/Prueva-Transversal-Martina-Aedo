def menu():
    print("""
        ******MENU PRICIPAL*********
        1.stock marca    
        2.Busqueda por precio   
        3.Actualizar precio
        4.Salir   
          """)
    opc = input("Ingrese una opcion: ")
    return opc




def stock_marca(productos,stock):
    marca  = input("Ingrese una marca (lenovo,Asus,HP,Dell): ").upper()
    validador = False   

    print (f" Marca Imgresada: {marca}")
    for codigo, datos in productos.items():
        if datos[0].upper() == marca:
            validador == True
            print (f" Marca:    {datos[0]}")
        
        if datos[0] in stock:
            modelo,(precio, stock) = stock[datos[0]]
            print (f"El stock es: {stock[1]}")

        
def busqueda_precio (productos,stock):

    pmin = input("Ingrese el precio minimo")
    pmax = input("Inrese el precio maximo")

    try:
        pmin = int(pmin)
        pmax = int(pmax)
    except ValueError:
        print ("Error. Debe ingresar numero entero")
        return 
    

    
lista = [] 


def Actualizar_precio (productos,stock):
    while True:
        modelo = input("Ingrese el modelo: ").upper().strip()

        if modelo in stock:
            validador = True
            modelomarca = lista[stock][0]
            precioantiguo = lista[stock][0]
            
        print (f" Modelo ingresado {modelo}")
        print (f" Precio {precioantiguo} ")

        actPrecio = int(input("Ingrese el valor nuevo: "))
        lista.append(actPrecio)
        pregunta = input("Desea actualizar otro precio (s/n)")      

        if pregunta != "s":
            break    
            



