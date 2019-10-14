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

# if the server recieves GET /bmi
@app.route('/bmi')
def show_bmi_form():
    return render_template("bmi.template.html")
    

@app.route('/bmi', methods=['POST'])
def process_bmi_form():
    print(request.form)
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    bmi = weight / (height * height)
    return render_template('bmi_result.template.html', actual_bmi=bmi)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)