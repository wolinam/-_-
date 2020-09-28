sum = 0
num1,num2=0,0
char = ""

while(True):
    num1 = int(input("첫 번째 수 "))
    num2 = int(input("두 번째 수 "))
    char = input("계산할 연산자 (+,-,*,/ 중에서 입력): ")
    
    if(char == "+"):
        print ("%d + %d = %d\n"%(num1,num2,num1+num2))
    elif(char == "-"):
        print ("%d - %d = %d\n"%(num1,num2,num1-num2))
    elif(char == "*"):
        print ("%d * %d = %d\n"%(num1,num2,num1*num2))
    elif(char == "/"):
        print ("%d / %d = %5.2f\n"%(num1,num2,num1/num2))
    else:
        print("+,-,*,/ 중에서 입력하세요")
