from flask import Flask, render_template, request
from data import Students

app=Flask(__name__)

getStudents = Students()

@app.route('/students')
def stud():
        return render_template('studentlist.html',myStudentList=getStudents)

@app.route('/send',methods=['GET','POST'])
def send():
    if(request.method=='POST'):
        getName=request.form['name']
        getEmail=request.form['email']
        return render_template('result.html',newName=getName,newEmail=getEmail)

@app.route('/contact')
def con():
    return render_template('contactus.html')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/contact')
# def contact():
#     return render_template('contactus.html')


if(__name__=='__main__'):
    app.run(debug=True)