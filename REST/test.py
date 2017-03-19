from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods = ['post','get'])
def student():
    return render_template('home.html')

@app.route('/addSwitch',methods = ['get'])
def addSwitch():
    return render_template('test.html')

@app.route('/test2',methods = ['POST', 'GET'])
def test2():
    if request.method == 'POST':
        result = request.form['Name']
        return render_template("test2.html",result = result)

if __name__ == '__main__':
    app.run('0.0.0.0', 3005)
