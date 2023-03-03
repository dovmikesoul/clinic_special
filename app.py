from flask import Flask, render_template

#from config import config

app = Flask(__name__)

@app.route('/')
def index_():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/login.html')
def Login():
    return render_template('auth/login.html')


if __name__=='__main__':
    app.run(port=5000, host="0.0.0.0")