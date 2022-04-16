from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def addForm():
    return render_template("addForm.html")


@app.route("/addStatement", methods=["POST"])
def addStatement():
    date = request.form["date"]
    name = request.form["title"]
    amount = request.form["amount"]
    category = request.form["category"]
    print("Date =", date, "Title =", name,
          "Amount =", amount, "Category =", category)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
