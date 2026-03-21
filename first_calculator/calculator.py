from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None

    if request.method == "POST":
        
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        operation = request.form["operation"]
        if num1 and num2:
            num1 = float(num1)
            num2 = float(num2)
        if operation == "add":
            result = num1 + num2
        elif operation == "sub":
            result = num1 - num2
        elif operation == "mul":
            result = num1 * num2
        elif operation == "div":
            result = num1 / num2

    return render_template("login.html", result=result)

app.run(debug=True)
