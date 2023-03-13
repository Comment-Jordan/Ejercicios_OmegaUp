n= int(input("Ingrese el número de edade por registrar: "))
arreglo=[]

for i in range(n):
    edad= int(input("Ingrese edad {} : ".format(i+1)))
    arreglo.append(edad)

arreglo2=set(arreglo)
arreglo_chido=list(arreglo2)


for m in arreglo_chido:
    print("El número",m,"se repite:",arreglo.count(int(m)), "veces")    