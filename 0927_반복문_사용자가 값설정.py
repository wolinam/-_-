i, sum = 0,0
num1,num2,num3 = 0,0,0

num1 = int(input("시작값 설정 : "))
num2 = int(input("끝값 설정 : "))
num3 = int(input("증가값 설정 : "))

for i in range(num1, num2+1, num3):
    sum += i
    
print("%d " % sum)
