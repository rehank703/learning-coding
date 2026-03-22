from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    submitted = None
    response = None
    if request.method == "POST":
        user_input = request.form.get("user_input")
        submitted = "submitted"
        response = "Bot:" + random.choice(["Hello world", "hello worldddd", "helllo worlld!", "Heeelo worlldd"])
        return render_template("chat.html", response=response, submitted=submitted)
    return render_template("chat.html", response=response, submitted=submitted)

app.run(debug=True)