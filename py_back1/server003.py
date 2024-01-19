from flask import Flask,request,render_template
import datetime

#태어난 년도를 입력받아 나이를 출력

app = Flask(__name__)

@app.route("/nai_view")
def nai_view():
    return render_template("year_main.html")



@app.route("/nai_result")
def nai_result():
    val1 = int(request.args["val1"])
    num = (int(datetime.datetime.now().year) - val1) + 1
    return render_template("year_result.html", result = num)



app.run()

# http 상태코드
# 200 - 연결 성공 - 오류없음
# 400 - 잘못된 요청(작업시작x)
# 403 - 권한이 없음
# 404 - 파일이 없음(not found)
# 405 - 메소드가 오류(get,post)
# 500 - 작업중 오류