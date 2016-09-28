from flask import Flask, render_template # web framework
app = Flask(__name__)
import blink_lib


@app.route('/') # URL
def home():
    data = {}
    return render_template('home.html', data=data)

@app.route('/led/<status>') # URL
def led(status): # function
    status_bool = False
    if status == 'on':
        status_bool = True
    data = {
        'status': status,
        'name': 'Hugo',
    }
    blink_lib.led(status_bool)
    return render_template('led.html', **data)

@app.route('/led_random') # URL
def Led_random(): # function
    data = {}
    status = blink_lib.led_random()
    data = {
        'random_status': status
    }
    return render_template('led_random.html', **data)

if __name__ == '__main__':
    # accessible via:
    # http://raspberrypi.local:8000/
    app.run(host='0.0.0.0', port=8000)
