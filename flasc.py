from flask import Flask, render_template, redirect, request
from main import *
from person import acquireData
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/display/')
def render_static():
    return app.send_static_file("results")

@app.route('/query', methods=['POST'])
def query():
	#acquireData(request.form['spreadsheet id'])
	main(request.form['spreadsheet id'])
	return redirect('/display/')

if __name__ == '__main__':
    app.run()