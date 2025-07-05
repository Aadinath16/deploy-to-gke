from flask import Flask
app = Flask(__name__)

@app.route("/hello1")
def hello():
    return "Hello from Flask-1 on GKE!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # nosec B104
