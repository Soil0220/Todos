#뷰 설계 : 웹 스토리보드를 작성해야한다.
#모델 설계 : 데이터의 구조
#코딩

import flask as f
import model as m


#플라스크 앱(백엔드 서버)을 생성, 인자는 현재파일의 이름
app = f.Flask(__name__)

@app.route("/", methods=["get"])
def list():
    """
    방명록 출력
    """
    guestbook = m.findall()
    #list.html에 넘길건데 list라는 이름으로 넘김
    return f.render_template("list.html", list = guestbook)

@app.route("/write", methods=["post"])
def write():
    content = f.request.form.get("content",type=str)
    m.save(content=content)
    return f.redirect("/")

@app.route("/delete", methods=["post"])
def delete():
    gno = f.request.form.get("gno", type=int)
    m.delete(gno)
    return f.redirect("/")

#서버를 개발자모드(변경하면 자동 재실행)로 실행
app.run(debug=True)
