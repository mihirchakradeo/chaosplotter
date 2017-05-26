from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('main.html')

@app.route('/plot',methods=['GET','POST'])
def plot():
	x = request.form['x']
	y = request.form['y']
	iter = request.form['iter']
	return render_template('index.html',x=int(x),y=int(y),iter=int(iter))


if __name__ == '__main__':
	app.run(debug=True)