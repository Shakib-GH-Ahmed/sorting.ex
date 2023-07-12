x=open("input4.txt","r")
y=open("output4.txt","w")

first=int(x.readline().strip())
lst=x.readline().split()
lst=[int(i) for i in lst]
third=int(x.readline().strip())

def smallest(lst,start,end,val):
    if start==end:
        return lst[start]
    
    call= pivot_partition(lst,start,end)
    num= call - start +1
    if num==val:
        return lst[call]
    elif num > val:
        return smallest(lst,start,call-1,val)
    return smallest(lst,call+1,end,val-num)

def pivot_partition(l,start,end):
    piv=l[end]
    c=start-1
    for i in range(start,end):
        if l[i] <= piv:
            c+=1
            l[c],l[i]=l[i],l[c]
    l[c+1],l[end]=l[end],l[c+1]
    return c+1

for i in range(third):
    next=int(x.readline())
    store=smallest(lst,0,len(lst)-1,next)
    if i==third-1:
        y.write(f"{store}")
    else:
        y.write(f"{store}\n")
        
y.close()