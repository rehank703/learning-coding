#import main packages
from flask import Flask, request, Response, redirect, url_for, session

#define flask
app = Flask(__name__)

#secret key
app.secret_key= "superkey"

#login page
@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "rehan" and password == "786":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return "incorrect password try again!!"
    return '''
            <h2>Login here !!</h2>
            <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type ="text" name="password"><br>
            <input type="submit" value="Login">
            </form>
'''

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
    <h2>Welcome user {session["user"]}</h2>
    <a href={url_for("logout")}>logout</a>
       '''
    return redirect(url_for("login"))
     
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


app.run(debug=True)