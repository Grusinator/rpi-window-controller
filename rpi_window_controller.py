
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
	@app.route('/test/')
	def running_test():
		controller = WindowController()
		controller.run_test()
		return "Opening Window"

    app.run()

	