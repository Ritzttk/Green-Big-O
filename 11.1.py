n=int(input())
a=list(map(int,input().split()))



for i in range(1,n,1):
    #print(a[i])
    x=a[i]
    pos = i
    for j in range(i,-1,-1):
        if(j > 0 and a[j-1]>x):
            a[j]=a[j-1]
            a[j-1] = 0
            print(a)
        else:
            pos=j
            break
    a[pos]=x
    print(a)
print(a)





