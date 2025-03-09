from flask import Flask

app = Flask(__name__)

@app.route('/name')
def name():
    return "SIVA RAJESH C"

@app.route('/reg-no')
def register_number():
    return "22ITl06"

@app.route('/dept')
def department():
    return "Information Technology"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
