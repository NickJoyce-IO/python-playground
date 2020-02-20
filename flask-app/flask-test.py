from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.route('/')
def home():
    return "Hello, World!"

@app.route('/nick')
def nick():
    user = {'username' : 'Misty'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Misty'},
            'body': 'I want to play ball!'
        },
        {
            'author': {'username': 'Nick'},
            'body': 'Bloody Helston!'
        }]
    return render_template('index.html',title = 'Welcome', user=user, posts=posts)

if __name__ == '__main__':
    app.run(debug=True)