
from flask import Flask
# from WindowController import WindowController

app = Flask(__name__)

@app.route('/test/')
def running_test():
	# controller = WindowController()
	# controller.run_test()
	text = "running test"
	print(text)
	return text

@app.route('/')
def default():
	text = "default landing page"
	print(text)
	return text

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

	