a=[]
n= int(input())
for x in range(0,n):
    element=input()
    a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max1):
       max1=len(i)
       temp=i
print(max1)
