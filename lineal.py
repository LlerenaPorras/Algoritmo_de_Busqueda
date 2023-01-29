#Busqueda Lineal
listaL=[1,3,5,7,9,11,13,17,21]
totalLargo=len(listaL)
print(listaL)
buscarA = int(input("Ingrese un numero abuscar en la lista: "))
def lineal (valor):
     encontrado=-1
     for i in range(totalLargo):
          if(listaL[i]== buscarA):
               encontrado=i
               return f"Se encuentra en la posicion: {encontrado}"
          

print(lineal(buscarA))


     
     