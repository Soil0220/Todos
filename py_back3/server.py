from flask import Flask,request,render_template


app = Flask(__name__)


@app.route("/info", methods=["get"])
def input_info():
    return render_template("main.html")

@app.route("/info", methods=["post"])
def output_info():
    val1 = request.form["val1"]
    val2 = request.form["val2"]
    return render_template("result.html", result1 = val1, result2 = val2 )

app.run(debug = True)

#통신규약 : protocol
#인터넷은 많은 통신규약들의 집합
#웹에서 사용하는 프로토콜이 http
#http 상태코드
# 200 :ok
# 300대 : (이동할 곳이 없어요)
# 400 : request오류(입력실패)
# 403 : 권한오류
# 404 : 페이지가 없음
# 405 : 메소드오류
# 500 : 서버쪽 처리오류(입력은성공)
