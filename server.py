from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)
@app.route('/')
def hellodude():
    return render_template('index.html') 
@app.route('/<string:page_name>')
def hellme(page_name):
    return render_template(page_name)
def writeData(data):
    with open('database2.csv', mode='a', newline='') as database:
        name=data['Name']
        subject=data['Subject']
        message=data['message']
        writers = csv.writer(database, delimiter=',', quotechar='"')
        writers.writerow([name, subject, message])

@app.route('/submited', methods=['POST', 'GET'])
def submitedForm():
    if request.method == 'POST':
        data=request.form.to_dict()
        writeData(data)
        return redirect('/thanku.html')
    else:
        return 'wrong dude try again'
