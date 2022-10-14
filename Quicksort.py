def partition (a,low,high):
    pivot = a[high]
    i=low-1
    for j in range(low,high):
        if a[i]<=pivot:
            i=i+1
            a[i+1],a[high]=a[high],a[i+1]
            
        
    return i+1
def quicksort(a,low,high):
    if low<high:
        pi=partition(a,low,high)
        quicksort(a,low,pi-1)
        quicksort(a,pi+1,high)
a=[]
for i in range(int(input("enter the size:"))):
    a.append(int(input("enter elements:")))
quicksort(a,0,len(a)-1)
print(a)
