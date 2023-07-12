x=open("input1.txt","r")
y=open("output1.txt","w")

line1=x.readline().strip()
line1=int(line1)
lst=x.readline().split()

def alien(lst,i,line1):
    i=i
    j=i+1
    c=0
    for run in range(line1):
        if i==len(lst)-1:
            break
        if j!=len(lst):
            if int(lst[i]) > int(lst[j]):
                c+=1
                j+=1
            else:
                j+=1
    if i!=len(lst)-1:
        val=c + alien(lst,i+1,line1)
        return val
    else:
        return c

total_aliens=alien(lst,0,line1)
y.write(f"{total_aliens}")

y.close()