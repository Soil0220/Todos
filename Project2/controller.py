#프로그래밍==문서화

# 익명 게시판

# R get / findall
#   get /read findone
# C get /write
#   post /write save


#요소
#제목 내용 닉네임 날짜 조회수

from flask import Flask,request,render_template,redirect
import dao



app=Flask(__name__)

@app.route("/")
def root():
    """
    초기진입화면
    전체 글 보기
    """
    return render_template("root.html",list = dao.findall())

@app.route("/read")
def read():
    """
    글 하나 읽기
    """
    bno = request.args.get("bno", type=int)
    b_item = dao.findone(bno)
    return render_template("individual_read.html", list_item = b_item)

@app.route("/write")
def write():
    """
    글 작성 페이지
    """
    return render_template("individual_write.html")

@app.route("/write", methods=["post"])
def write_post():
    """
    글 작성버튼 클릭
    """
    title = request.form.get("title", type=str)
    content = request.form.get("content", type=str)
    nickname = request.form.get("nickname", type=str)
    dao.save(title=title,content=content,nickname=nickname)
    return redirect("/")



app.run(debug=True)