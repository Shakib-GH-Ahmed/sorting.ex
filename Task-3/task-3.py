x=open("input3.txt","r")
y=open("output3.txt","w")

line1=x.readline().strip()
line1=int(line1)
given_lst=x.readline().split()

def quicksort(lst,l,h):
    if l<h:
        val=pivot_partition(lst,l,h)
        quicksort(lst,l,val-1)
        quicksort(lst,val+1,h)
        
def pivot_partition(lst,f,l):
    piv=int(lst[f])
    first=f+1
    last=l
    while True:
        while first <= last and int(lst[first]) <= piv:
            first+=1
        while first <= last and int(lst[last]) >= piv:
            last-=1
        if last < first:
            break
        else:
            lst[first],lst[last]=lst[last],lst[first]

    lst[f],lst[last]=lst[last],lst[f]
    return last


l=0
h=len(given_lst)-1
quicksort(given_lst,l,h)

for i in range(line1):
    if i == line1-1:
        y.write(given_lst[i])
    else:
       y.write(given_lst[i]+' ') 
       
       
y.close()
