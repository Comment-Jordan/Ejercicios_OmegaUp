import string

alfabeto=list(string.ascii_lowercase)

cadena=input("Ingrese palabra: ")
contador=[]

i=0
for palabra in alfabeto:
    if(palabra!=alfabeto[i]):
        contador.append(0)
        i+=1
    else:
        conta=cadena.count(palabra)
        contador.append(conta)
        i+=1        
print(contador)
#print(alfabeto)
j=0
for letra in alfabeto:
    if(alfabeto[j] in cadena):        
        print("La letra",letra,"aparece:",cadena.count(letra),"veces")
        j+=1
    else:      
        j+=1