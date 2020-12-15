phone = {}
while(True):
    a = input('1) 전화번호 저장, 2) 전화번호 검색 ')
    if(a=='1'):
        name = str(input('저장할 사용자의 이름을 입력하세요. '))
        num = str(input('전화번호를 입력하세요. '))
        phone[name]=num
    elif(a=='2'):
        name = str(input('검색할 사용자의 이름을 입력하세요. '))
        if name in phone:
            print(phone[name])
        else:
            print('존재하지 않는 사용자 입니다.')
    elif(a=='끝'):
        break
    else:
        print('1과 2중에 선택해주세요.')
        continue
