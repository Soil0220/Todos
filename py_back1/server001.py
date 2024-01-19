from flask import Flask, request

"""
back
"""

#class -> 사용자정의 자료형을 만드는 방법

#__name__은 현재 파일의 이름 -> Flask객체를 생성
#서버는 사용자 요청을 기다리다가 요청이 들어오면 처리해주는 프로그램이다.
#Flask웹서버는 5000번 포트로 사용자 요청을 대기한다.

app = Flask(__name__)


#decorator라고함
#자바에선 annotation이라고함
@app.route("/html")
def hello():
    """
    hello를 출력
    """
    return "hello flask"

@app.route("/hello2")
def insa():
    return "안녕하세요"

@app.route("/hello3")
def add():
    val = request.args["val"]
    # request.args라는 dictionary안에 값형태로 쿼리문의 내용을 넣는다.
    return val


@app.route("/hello4")
def 제곱():
    val = int(request.args["val"])
    # 기본적으로 request의 값은 글자다
    # 최종출력도 str형식이여야한다. (안하면 오류코드 500)
    return str(val * val)


#적정체중 = 키-105라고 할 때
#키를 입력받아 적정체중을 출력하는 서버프로그램 작성

@app.route("/체중계산")
def calculator():
    val = int(request.args["val"])
    result = val - 105
    return f"당신의 키 : {val}, 적정체중 : {result}입니다."




app.run()