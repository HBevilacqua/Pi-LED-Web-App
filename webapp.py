from flask import Flask, render_template # web framework
from threading import Thread
app = Flask(__name__)
import blink_lib

thread_blink = None

@app.route('/') # URL
def home():
    data = {}
    return render_template('home.html', data=data)

@app.route('/led') # URL to chose the mode
@app.route('/led/<status>') # on/off mode URL
def led(status = None): #None : optional parameter
    status_bool = False
    if status is not None and status == 'on':
        status_bool = True
    data = {
        'status': status,
    }
    blink_lib.led(status_bool)
    return render_template('led.html', **data)

@app.route('/led_random') # Random mode URL
def Led_random(): # function
    data = {}
    status = blink_lib.led_random()
    data = {
        'random_status': status
    }
    return render_template('led_random.html', **data)


@app.route('/led_blink') # Blink mode URL
def Led_blink(): # function
    data = {}
    global thread_blink
    # if the thread is not running, starts the thread
    if (thread_blink is None) or (not thread_blink.isAlive()):
        thread_blink = blink_lib.Led_thread("thread_blink")
        thread_blink.start()
    thread_status = thread_blink.isAlive()
    # dummy return
    data = { 'status': thread_status }
    return render_template('led_blink.html', **data)


if __name__ == '__main__':
    # accessible via:
    app.run(host='0.0.0.0', port=8000, debug=True)
