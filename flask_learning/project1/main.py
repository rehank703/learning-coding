from flask import Flask, render_template, request

app = Flask(__name__)


def evaluate_expression(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        return str(result)
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except Exception:
        return "Invalid input"


@app.route("/", methods=["GET", "POST"])
def home():
    display = ""

    if request.method == "POST":
        display = request.form.get("display", "")
        button = request.form.get("button", "")

        if button == "C":
            display = ""
        elif button == "=":
            display = evaluate_expression(display) if display else ""
        else:
            display += button

    return render_template("index.html", display=display)


if __name__ == "__main__":
    app.run(debug=True)
