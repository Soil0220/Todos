#redirect : post, 처리하고 새주소로이동
#render_template : get, html을 출력


from flask import Flask,request,redirect,render_template

app = Flask(__name__)

#전역변수 : 모든 함수가 접근가능한 공유데이터
todos = []
tno = 1

#내용을 출력하는 페이지
@app.route("/list")
def list():
    return render_template("list.html", todos=todos)
#웹페이지는 페이지 단위로 진입하는 부분을 만들어 두는게 좋다.
#웹페이지를 표시하기 위한 최소한의 값이 필요할 수도있고 추후 개발확장을
#위해서라도 진입단위를 만들고 페이지에 연결할 때는 render로 연결이 아닌 리다이렉트로연결



@app.route("/list",methods=["post"])
def list_delete():
    result = request.form.get("tno",type=int)
    for index, todo in enumerate(todos):
        if result == todo["tno"]:
            del todos[index]
            break
    return redirect("/list")


@app.route("/write")
def write_input():
    return render_template("write.html")

@app.route("/write", methods=["post"])
def do_write():
    global tno
    title = request.form.get("title",type=str)
    todo={"tno":tno,"title":title,"finish":False}
    todos.append(todo)
    tno=tno+1
    return redirect("/list")
#

app.run(debug=True)