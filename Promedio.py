n=int(input())
cadena=input().split()
resu=0
for i in range(n):
    resu+=int(cadena[i])
print(resu/n)