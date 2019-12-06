import os

from flask import Flask, request

from WindowController import WindowController

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'user'
app.config['BASIC_AUTH_PASSWORD'] = PASSWORD = os.environ.get('API_PASSWORD') or "verySecure2019"
app.config['BASIC_AUTH_FORCE'] = True

controller = WindowController()

@app.route('/test/')
def running_test():
    controller.run_test()

    return "running test"


@app.route('/open/')
def open_window():
    controller.open_window()
    return "opening"

@app.route('/ventilate/')
def open_window():
    min = request.args.get('min')
    controller.timed_ventilation(min)
    return "opening"


@app.route('/close/')
def close_window():
    controller.close_window()

    return "closing"


@app.route('/')
def default():
    return "default landing page"


@app.route('/stop/')
def stop():
    controller.STOP = True
    return "stop"


if __name__ == '__main__':
    app.run(debug=False, port=250, host='0.0.0.0')
