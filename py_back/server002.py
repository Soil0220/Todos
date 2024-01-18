from flask import Flask,request,render_template

app = Flask(__name__)



#사용자가 입력한 값을 html로 출력
@app.route("/sample1")
def sample1():
    val = request.args["val"]
    return render_template("sample1.html",result=val)
#templates로 폴더이름이 고정되어야함
app.run()