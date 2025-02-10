from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None
    expression = ""

    if request.method == "POST":
        expression = request.form.get("expression", "")
        try:
            # Evaluate mathematical expressions securely
            result = eval(expression, {"__builtins__": None}, {
                "sqrt": math.sqrt,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "log": math.log,
                "pi": math.pi,
                "e": math.e,
                "pow": pow,
                "abs": abs
            })
        except Exception as e:
            error = "Invalid input. Please try again."

    return render_template("calculator.html", result=result, error=error, expression=expression)

if __name__ == "__main__":
    app.run(debug=True)
