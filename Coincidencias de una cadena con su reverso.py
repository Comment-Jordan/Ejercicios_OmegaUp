cadena=input().upper().replace(" ","")
nueva_cadena=""
contador=0
if(len(cadena)<=1000):

    for i in (reversed(cadena)):
        nueva_cadena=nueva_cadena+i
    for i in range(len(cadena)):   
        if(cadena[i]==nueva_cadena[i]):
            contador+=1
else:
    pass            
print(contador)