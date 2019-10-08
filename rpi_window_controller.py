import asyncio
from flask import Flask

from WindowController import WindowController

app = Flask(__name__)
controller = WindowController()


@app.route('/test/')
def running_test():
    asyncio.run(controller.run_test())
    return "running test"


@app.route('/open/')
def open_window():
    asyncio.run(controller.open_window())
    return "opening"


@app.route('/close/')
def close_window():
    asyncio.run(controller.close_window())
    return "closing"


@app.route('/')
def default():
    return "default landing page"


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
