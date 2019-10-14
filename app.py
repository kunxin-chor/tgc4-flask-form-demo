from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/', methods=['POST'])
def process_form():
    print (request.form)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    return render_template('hello.template.html', fn=first_name, ln=last_name)

@app.route('/about-us')
def about():
    return "About Us"

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)