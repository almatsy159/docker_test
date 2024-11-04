from flask import Flask,render_template as rt

app = Flask(__name__)

@app.route("/")
def index(args:dict = None):
    print(args)
    return rt('index.html',args=args)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=2044,debug=True)