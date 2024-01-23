"""
data model
"""

import datetime

bulletin_board = []
bno = 1

def save(title,content,nickname):
    """
    저장
    """
    date = datetime.datetime.now().date()
    global bno
    b_item = {"bno" : bno, "title" : title, "content" : content, "date" : date, "nickname" : nickname,"viewcount" : 0}
    bulletin_board.append(b_item)
    bno+=1

def findall():
    """
    목록 출력
    """
    return bulletin_board


def findone(bno):
    """
    글 출력
    """
    for b_item in bulletin_board:
        if b_item["bno"] == bno:
            b_item["viewcount"] += 1
            return b_item