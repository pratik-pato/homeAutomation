import Adafruit_BBIO.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
led = "P8_10"
GPIO.setup(led,GPIO.OUT)
@app.route('/switch.html', methods=['GET','POST'])
def change_LED_state():
    if request.method == 'POST':
        current_state = request.form['state']
        print current_state
        if (current_state == 'on'):
            GPIO.output(led,GPIO.HIGH)
        elif (current_state == "off"):
            GPIO.output(led,GPIO.LOW)
    return render_template('switch.html')
app.run('0.0.0.0', 3005)
