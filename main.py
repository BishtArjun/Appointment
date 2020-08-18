from flask import Flask, request, render_template, url_for, jsonify

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

@app.route('/process', methods=['POST'])
def process():

	name = request.form['name']
	date = request.form['date']

	if name and email:
		newName = Name

		return jsonify({'name' : newName})

	return jsonify({'error' : 'Missing data!'})


if __name__ == "__main__":
    app.run(debug=True)
