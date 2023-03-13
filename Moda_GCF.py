n= int(input("Ingrese n: "))
l= input("Ingrese cadena de números con espacio entre número: ")
max=-1000000000
nummax=0

for i in range(len(l)):    
    if l[i]!=" ":        
        compara=l.count(l[i])
        if(compara>max):
            max=compara
            nummax=l[i]

print(nummax)