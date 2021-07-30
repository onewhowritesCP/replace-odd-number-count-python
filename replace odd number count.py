l=[222,3,35,62,124,61,29,375,66,7,-1]
count = 0
for i in range(0,len(l)):
    if l[i]%2!=0 and i!=len(l)-1:
        count +=1
    else:
        if count > 1:
            l[i-1]=count
            while count != 1:
                l[i-count]= -1
                count -= 1
        count = 0
l = [i for i in l if i>=0 ]

print(l)
