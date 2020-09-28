sum ,i=0,0

for i in range(1,100,2):
    sum += i
    
    if (sum>=600):
        break
print("1~100까지의 홀수의 합에서 600을 넘어갈 때의 합계 값 : %d \n 증가되던 숫자 : %d"%(sum, i))
