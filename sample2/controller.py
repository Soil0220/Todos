"""
controller
"""

from flask import Flask,request,render_template,redirect
import model as m


app = Flask(__name__)


@app.route("/")
def start_list():
    """
    초기진입
    """
    return render_template("list.html", daiji=m.zen)

@app.route("/write", methods=["post"])
def write():
    """
    작성
    """
    server_content = request.form.get("content", type=str)
    server_name = request.form.get("name", type=str)
    m.save(server_content, server_name)
    return redirect("/")



@app.route("/delete", methods=["post"])
def delete():
    """
    삭제
    """
    tno = request.form.get("tno", type=int)
    m.data_delete(tno)
    return redirect("/")

@app.route("/update", methods=["post"])
def update():
    """
    삭제
    """
    tno = request.form.get("tno", type=int)
    content = request.form.get("content", type=str)
    m.update(tno,content)
    return redirect("/")

app.run(debug=True)