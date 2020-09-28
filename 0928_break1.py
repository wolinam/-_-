sum = 0
num1,num2=0,0

while(True):
    num1 = int(input("더할 첫 번째 수 "))
    if num1==0:
        break
        
    num2 = int(input("더할 두 번째 수 "))
    print ("%d + %d = %d\n"%(num1,num2,num1+num2))
    
print("0을 입력해 반복문을 탈출했습니다.")
