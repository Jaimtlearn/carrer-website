from flask import Flask, render_template, jsonify

app = Flask(__name__)

Jobs = [{
    'id': '1',
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'sallary': 'Rs. 10,00,000'
}, {
    'id': '2',
    'title': 'DevOps Engineer',
    'location': 'Bengaluru, India',
    'sallary': 'Rs. 20,00,000'
}, {
    'id': '3',
    'title': 'Python Dev',
    'location': 'Ahmedabad, India',
    'sallary': 'Rs. 5,00,000'
}, {
    'id': '4',
    'title': 'QA Analyst',
    'location': 'Remote',
}]


@app.route('/')
def Home():
  return render_template("home.html", jobs=Jobs)


@app.route('/api/jobs')
def data():
  return jsonify(Jobs)


if __name__ == "__main__":
  app.run(host="0.0.0.0")
