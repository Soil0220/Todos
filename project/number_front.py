
"""
front
"""


import number_back as n

while True:
    print("************")
    print("1. 숫자 추가")
    print("2. 숫자 출력")
    print("999.종료")
    select = input("메뉴선택 : ")
    if select == "1":
        num = int(input("숫자 입력"))
        n.save(num)
    elif select == "2":
        print(n.find_all())
    elif select == "999":
        print("감사합니다.")
        break