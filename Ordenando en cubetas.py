n=int(input("Ingrese n: (número de pelotas) "))
m=int(input("Ingrese m: (número de color máximo) "))
entrada= [n]


while True:
    
    if(len(entrada)>n):
        break         
    
    elif (inserte<m):            
        inserte= int(input("Ingrese color de pelota: "))
        entrada.append(inserte)                               
    elif(inserte>m): 
        print("Ingrese color de pelota válido")
        
        
for j in range(1,len(entrada)):
    print(j,":",entrada.count(j))

