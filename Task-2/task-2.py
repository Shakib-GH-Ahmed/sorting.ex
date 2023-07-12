x=open("input2.txt","r")
y=open("output2.txt","w")

line1=x.readline().strip()
line1=int(line1)
given=x.readline().split()
for i in range(line1):
    given[i]=int(given[i])

def max_num(lst):
    if len(lst)==1:
        return lst[0]
    if len(lst)==2:
        return lst[0] + lst[1]**2
    
    left_subarray=max_num(lst[0:len(lst)//2])
    right_subarray=max_num(lst[len(lst)//2:])
    both_max_num=max(lst[0:len(lst)//2]) + cross_max(lst[len(lst)//2:len(lst)-1])
    return max(left_subarray,right_subarray,both_max_num)

def cross_max(lst):
    new=int(lst[0])**2
    for item in range(len(lst)):
        store=int(lst[item])**2
        if store > new:
            new=store
    return new

value=max_num(given)
y.write(f"{value}")

y.close()
