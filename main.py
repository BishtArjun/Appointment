from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("appointment.html")

@app.route("/admin")
def about():
    return render_template("admin.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)
