sum ,i=0,0

for i in range(1,100,1):
    sum += i
    
    if(sum>=1000):
        break
print("1부터 더했을 때, 1000이상이 되는 시점은 숫자 %d 입니다."% i)
