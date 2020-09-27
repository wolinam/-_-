f0=0
f1=1
f=0
mem1 = f0
mem2 = f1

print("%d %d"%(f0,f1), end = " ")
for i in range(2,10,1):
    f=mem1+mem2
    mem1=mem2
    mem2=f
    print("%d"%(f), end = " ")
