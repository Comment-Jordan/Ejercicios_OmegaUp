n= int(input())

for m in range(n):    
    x=input() 
    total=0
    num=0
    while len(x)>1:
        total=0
        for i in x:
            num=int(i)
            total=total+num
            x=str(total)                       
    print(x)         