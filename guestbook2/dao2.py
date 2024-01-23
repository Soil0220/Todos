#게시판 dao 작성

board_list = []
bno = 1

#게시판은 글 번호,제목,내용,글쓴이로 구성

#save

def save(title,content,nickname):
    """
    저장
    """
    global bno
    bb = {"bno" : bno,"title" : title, "content" : content, "nickname" : nickname, "readcount" : 0}
    board_list.append(bb)
    bno+=1
    return True

def findall():
    """
    findall
    """
    return board_list


def delete(bno):
    """
    delete
    """
    for i in board_list:
        if i["bno"] == bno:
            board_list.remove(i)
            return True
    return False