#Busqueda Binaria 
listaB=[0,55,44,33,29,18,17,32,30,12,99,77]
listaB.sort() 
largoLb=len(listaB)
print(listaB)
z = int(input("Ingrese un numero abuscar en la lista:\n"))

def binaria (valor):
     inicio=0
     final = largoLb-1
     while inicio <=final:
          puntoMedio= ((inicio+final)//2)

          if valor == listaB[puntoMedio]:
               return  puntoMedio
          elif valor >listaB[puntoMedio]:
               inicio= puntoMedio+1
          else :
               final = puntoMedio-1
     return None

def buscarValor(valor):
     resBusqueda = binaria(valor)
     if resBusqueda is None:
          return f"El numero {valor} no se encontro"
     else:
          return f"El numero {valor} se encuntra en la posicion  {resBusqueda}"


print(buscarValor(z))
