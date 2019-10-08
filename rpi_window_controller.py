from flask import Flask

from WindowController import WindowController

app = Flask(__name__)
controller = WindowController()


@app.route('/test/')
def running_test():
    controller.run_test()

    return "running test"


@app.route('/open/')
def open_window():
    controller.open_window()

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
    return "default landing page"


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
