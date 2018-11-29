from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "OK"
 
@app.route("/hello/<string:name>")
def hellouser(name):
    return "Hello {}".format(name)
 
if __name__ == "__main__":
    app.run()
