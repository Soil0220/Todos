# 웹 프로그래밍
# - 서버(server)->대기->호출->서버
#   url과 port를 가져야함

#사용자의 요청에 응답하는 서버 : 백엔드 + 화면
# 프레임워크 -필요한 기능들을 부품화해서 조합하는 방식
# templates - html, static - css,js 


from flask import Flask,request,render_template

app = Flask(__name__)

# 배포 서술자(deployment descriptor : 함수와 주소의 쌍)
@app.route("/name_ex")
def name_ex():
    #플라스크 함수의 리턴은 반드시 문자열이여야한다.
    return render_template("name_ex.html")

@app.route("/calculate")
def calculate():
    val = request.args["val"]
    return val

#어떤 작업을 하려면 화면을 보여준다(get) + 결과를 출력한다.(post)
#이름을 입력받아 출력
@app.route("/name",methods=["get"])
def name_input():
    return render_template("name.html")

@app.route("/name",methods=["post"])
def name_print():
    #get형식 요청 데이터 : request.args
    #post형식 요청 데이터 : request.form
    name = request.form["name"]
    nai = request.form["nai"]
    return render_template("name_result.html", name=name, nai=nai)

#현재 서버의 모든 url을 출력
print(app.url_map)


# 실행되면 url:127.0.0.1:5000
#debug는 개발모드
app.run(debug=True)