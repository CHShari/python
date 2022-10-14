def sort(a):
    for i in range(1,len(a)):
        j=i-1
        e=a[i]
        while(a[j]>e) and j>=0:
            a[j+1]=a[j]
            j=j-1
            a[j+1]=e
    print(a)
n=int(input("enter no.of elements:"))
a=[]
for i in range(n):
    a.append(int(input()))
sort(a)
    
    
    
    
    
    
