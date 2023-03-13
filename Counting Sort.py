n= int(input("Ingrese n: "))
arreglo=[]

for i in range(n):
    inserte=int(input("Ingrese elemento:"))
    arreglo.append(inserte)

#Aqui ordeno mi lista
arreglo.sort()

print(arreglo)
cadena=""
for j in range(0, len(arreglo)):
    cadena+=str(j)+" "
    #cadena+=" " 
    #print(j)
print(cadena)