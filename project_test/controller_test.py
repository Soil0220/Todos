import flask as f
import dao_test as d
# Create  get/post    
# Read    get  
# Update  get(/read)/post
# Delete  get(/read)/post

# get   html을 보여준다
# post  처리 후 이동한다

#컨트롤러 구성
#1. 주소지정
#2. request에서 값을 꺼낸다.
#3. dao를 부른다.
#4. html 또는 redirect한다

app = f.Flask(__name__)

@app.route("/")
def list() :
    board_list = d.findall()
    return f.render_template("root.html", list=board_list)

@app.route('/write')
def 쓰기화면보여주기():
    return f.render_template("individual_write.html")

@app.route("/write", methods=['post'])
def 쓰기처리():
    nickname = f.request.form.get("nickname", type=str)
    title = f.request.form.get("title", type=str)
    content = f.request.form.get("content", type=str)
    d.save(nickname=nickname, title=title, content=content)
    return f.redirect("/")

@app.route("/read")
def 읽기():
    bno = f.request.args.get('bno', type=int)
    board = d.findone(bno)
    return f.render_template("individual_read.html",list_item=board)

# /read에서 내용을 바꾸고 변경버튼 클릭
@app.route("/update", methods=['post'])
def 변경():
    bno = f.request.form.get("bno", type=int)
    title = f.request.form.get("title", type=str)
    content = f.request.form.get("content", type=str)
    d.update(bno=bno, title=title, content=content)
    return f.redirect("/")

# /read에서 삭제버튼 클릭
@app.route("/delete", methods=['post'])
def 삭제():
    bno = f.request.form.get("bno", type=int)
    d.delete(bno=bno)
    return f.redirect("/")

app.run(debug=True)