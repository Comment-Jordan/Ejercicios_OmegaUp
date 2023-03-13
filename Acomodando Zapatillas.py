n= int(input("Ingrese n: "))
arreglo=[]

contador_quedar=0
contador_desechar=0

for i in range(n):
    k= int(input("Ingrese zapatilla {}: ".format(i+1)))
    arreglo.append(k)

arreglo2=set(arreglo)
arreglo_chido=list(arreglo2)

arreglo_desechar=[]
for j in range(len(arreglo_chido)):
    zapatillas= arreglo.count(arreglo_chido[j])
    if((zapatillas%2)!=0):
        contador_desechar+=1
        arreglo_desechar.append(arreglo_chido[j])
    elif(zapatillas%2==0):        
        contador_quedar+=1    
       
if(contador_quedar*2==n):
    print(":D")
else:
    print(arreglo_desechar)    

print("No se quedará con:",contador_desechar)
print("Se quedará con:",contador_quedar*2)