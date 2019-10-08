
from flask import Flask
from WindowController import WindowController

app = Flask(__name__)

@app.route('/test/')
def running_test():
	controller = WindowController()
	controller.run_test()
	text = "running test"
	print(text)
	return text

if __name__ == '__main__':
    app.run()

	