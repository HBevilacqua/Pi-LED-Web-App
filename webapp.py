from flask import Flask, render_template # web framework
app = Flask(__name__)
import blink_lib


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

if __name__ == '__main__':
    # accessible via:
    # http://raspberrypi.local:8000/
    app.run(host='0.0.0.0', port=8000)
