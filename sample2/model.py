"""
module
"""

import datetime


zen = []
tno = 1


def data_delete(tno):
    """
    제거
    """
    for item in zen:
        if item["tno"] == tno:
            zen.remove(item)
            break



def save(content : str, name : str):
    """
    저장
    """
    global tno
    date = datetime.datetime.now().date()
    dic = {"tno" : tno , "name" : name, "content" : content, "date" : date}
    zen.append(dic)
    tno += 1


def update(gno:int,content:str):
    """
    update
    """
    for item in zen:
        if item["tno"] == gno:
            item["content"] = content
            break
