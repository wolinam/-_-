stu = ['이황','이이','원효']
print('현재학생은',stu)
come = str(input("전학 온 학생은 누구입니까?"))
stu.append(come)
print(stu)

i = 0
for i in range(i,len(stu),1):
    print((i+1),stu[i],'\n')
