from flask import Flask, render_template, request

app = Flask(__name__)

comments = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        comments.append(request.form["comment"])

    return render_template("comments.html", comments=comments)

if __name__ == "__main__":
    app.run(debug=True)
