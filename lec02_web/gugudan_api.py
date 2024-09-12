from flask import Flask
from markupsafe import escape  # escape 할 때 이거 했어야 함!
from flask import request
app= Flask(__name__)



@app.route("/")
def hello():
    return 'Hello World!'

@app.route("/hello/<name>")
def say_hello(name):
    return f"안녕하세요. {escape(name)}"  #이게이게 안된다

@app.route("/dan/<dan>")
def gugudan_html(dan):
    html_str = ""
    for i in range(1,10):
        html_str += f"{dan} X {i} = {int(dan)*i}<br>"
    return html_str

@app.route("/gugudan/")
def gugudan_html2():
    dan =request.args.get("dan","2")
    html_str = ""
    for i in range(1,10):
        html_str += f"{escape(dan)} X {i} = {int(dan)*i}<br>"
    return html_str

app.run(debug=True)


#이거 코드 왜 안됨??_갓승원선배가 해결해줌!

# 다음주에 완성하기로 한 코드 있습니다.