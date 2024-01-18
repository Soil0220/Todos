"""
back 구현

"""

#front는 사용자와 입출력하는 view를 담당(터미널,웹,안드로이드,아이폰)
#데이터 자체는 원래는 백이 아니라 데이터 베이스에서 관리
#백은 처리를 담당하고, view에 상관없이 재사용하고 싶다.
#백을 재사용하려면 백에는 절대 view관련 코드가 있으면 안된다.


numbers = []

def save(num:int) -> bool:
    """
    파일 저장
    (input : int, output : bool)
    """
    if isinstance(num, int) is False:
        return False
    numbers.append(num)
    return True


def find_all()->list:
    """
    finde_all
    (input : none, output : list)
    """
    return numbers

def delete(num:int) -> bool:
    """
    delete
    (input : int, output : bool)

    """
    if isinstance(num, int) is False:
        return False
    for item in numbers.copy():
        if item == num:
            numbers.remove(item)
            return True
    return False
