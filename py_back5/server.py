from flask import Flask,request,render_template


app = Flask(__name__)


@app.route("/start",methods = ["get"])
def input():
    return render_template("start.html")


@app.route("/start",methods = ["post"])
def output():
    val = request.form.get("month",type=int)
    # type은 값을 특정 형식으로 바꿔서 받는다.
    return render_template("result.html", result = val)


#front에서 if문을 쓸 수도 있지만
#back에서 if문으로 val값에 따라 프론트를 다르게 할 수있다.

#season = "겨울"
#style = "blue"
#if 3 <= month<= 5:
#season = "봄"
#style = "purple"
#elif 6 <= month<= 8:
#season = "여름"
#style = "green"
#elif 9 <= month <= 11:
#season = "가을"
#style = "gray"
# season, style을 html에 보낸 후 html을 다음과 같이 간략화
#<p class = "{{style}}">{{season}}</p>

#urlencoded 형식
#?num=spring&nai=20 
#get 방식은 데이터 주소창에 나타남
#unlencoded 형식은 말 그대로 형식을 말하며
#get을 했을 때. 나오는 주소창의 ?~~~는 querystring이라고 한다.
#post 방식은 나타나지는 않는다. -> 보안이 중요할 때 좋다.


app.run(debug=True)

