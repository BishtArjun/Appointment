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
	data = request.json  ## find out why this is request.json, and not request.form 
	name = data['name']
	date = data['date']
	print('data from webpage =', name, date)


	return '' # we have to return thank you html page here

	

if __name__ == "__main__":
    app.run(debug=True)
