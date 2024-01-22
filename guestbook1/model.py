import datetime as d
gno = 3

#데이터 : model
guestbook = list()
gb1 = {"gno":1, "content":"첫번째 방명록", "writedate" : "2024-01-22"}

#파이썬에서 타입은 모두 클래스
#클래스 이름으로 객체를 생성할 수 있다.
#클래스 이름을 함수처럼 사용 가능.
gb2 = dict(gno = 2, content = " 두번째 방명록", writedate = "2024-01-22")

#def hap(val1:int, val2:int) -> int:
#    return val1 + val2

#hap(10, 20)
#val1에 10, val2에 20이 꼭 들어가야하면
#hap(val1=10,val2=20)
#변수의 수가 많아지면 위치를 기억할 수 없기에 순서에 관여하지않고 
#변수를 지정해서 넣을 수 있다.

guestbook.append(gb1)
guestbook.append(gb2)


def findall():
    """
    리스트 전부 출력 - 스프링은 모델 함수 이름이 정해져 있다.
    스프링처럼 써보겠음
    """
    return guestbook




def save(content : str):
    """
    저장
    """
    global gno
    writedate = d.datetime.now().date()
    gb = dict(gno=gno, content=content,writedate = writedate)
    guestbook.append(gb)
    gno+=1

def delete(gno : int):
    """
    제거
    """
    for gb in guestbook:
        if gb["gno"] == gno:
            guestbook.remove(gb)
            break

