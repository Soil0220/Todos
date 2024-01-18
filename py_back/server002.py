from flask import Flask,request,render_template

app = Flask(__name__)



#사용자가 입력한 값을 html로 출력
@app.route("/sample1")
def sample1():
    val = request.args["val"]
    return render_template("sample1.html",result=val)
#templates로 폴더이름이 고정된곳에 html을 만들어야함


#덧셈을 입력할 화면을 출력
@app.route("/add_view")
def sample2_view():
    return render_template("sample2_view.html")


@app.route("/sample2")
def sample2():
    val1 = int(request.args["val1"])
    val2 = int(request.args["val2"])
    return render_template("sample2.html",result = (val1+val2))
    # int형으로 변수를 줘도 인식한다.




app.run()