#이름과 나이를 입력받아 다음과 같이 출력한다.
#홍길동 님은 성년입니다.
#홍길동 님은 미성년입니다.
#단 성년 = 파랑색 미성년 = 빨강

from flask import Flask,request,render_template


app = Flask(__name__)


@app.route("/input_info", methods=["get"])
def input_info():
    return render_template("main.html")

#@app.route("/input_info2", methods="post")
#def out_info2():
#    return render_template("main.html2")


@app.route("/input_info",methods=["post"])
def output_info():
    irum = request.form.get("irum",type=str)
    nai = request.form.get("nai",type=int)
    is_adult= nai>=18
    return render_template("result.html", irum = irum, nai= nai, is_adult = is_adult)    


app.run(debug=True)