from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "chewon hello!"

@app.route("/hello")
def hello_world2():
    return "i'm hye jin  jjang!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
