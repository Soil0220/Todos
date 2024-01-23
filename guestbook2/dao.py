#웹 프로그래밍을 이렇게 만들자 :MVC
#MODEL : 데이터 -> model의 조직을 담당하는 파일(DAO)
#VIEW : 화면
#CONTROLLER : 모델,뷰 변경

#방명록 : 번호 닉네임 내용 작성일
#작업 : 작성 목록 삭제

import datetime
guestbook = []
gb = dict(gno=1,nickname="관리자",content="욕설,비방은 경고없이 삭제",writeday="2024-01-23")

guestbook.append(gb)

#일련번호는 보통 key로 사용된다.
#key는 보통 숫자

gno = 2

#crd
def save(nickname : str, content : str) -> bool:
    """
    save
    """
    global gno
    writeday = datetime.datetime.now().date()
    gb = dict(gno=gno, nickname=nickname, content=content, writeday=writeday)
    guestbook.append(gb)
    gno+=1
    return True

def findall() -> list:
    """
    findall
    """
    return guestbook

#return 함수를 종료하고 결과 값을 남겨라
def delete(gno : int) -> bool:
    """
    delete
    """
    for gb in guestbook:
        if gb["gno"]==gno:
            guestbook.remove(gb)
            return True
    return False

