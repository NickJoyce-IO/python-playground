from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/nick')
def nick():
    return 'Nick is an absolute hero!!!'

if __name__ == '__main__':
    app.run(debug=True)