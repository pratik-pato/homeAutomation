import switchOperations as swtch
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods = ['post','get'])
def student():
    return render_template('home.html')

@app.route('/addSwitch',methods = ['get','post'])
def addSwitch():
    return render_template('/switch/addswitch.html')

@app.route('/addswitchresult',methods = ['POST', 'GET'])
def addswitchresult():
    if request.method == 'POST':
        switch = request.form['switchName']
        port = request.form['portName']
        swtch.addSwitchInDb(switch,port)
        return render_template("/switch/addswitchresult.html",switch = switch,port = port)

if __name__ == '__main__':
    app.run('0.0.0.0', 3005)
