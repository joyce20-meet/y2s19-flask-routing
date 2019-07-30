from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/home page')
def home():
	return "WELCOME HOME" 
@app.route('/student/<int:student_id>/<string:name>/<int:student_year')
def student_id(student_id):
	return render_template(
		"student.html", student_id = student_id,)

if __name__ == '__main__':
    app.run(debug=True)
