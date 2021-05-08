from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html")

@app.route('/4')

def eight_by_four():
    return render_template("index2.html") 

@app.route('/<int:rows>/<int:columns>')

def customBoard(rows, columns):
    return render_template("index3.html", rows = rows, columns = columns) 


if __name__=="__main__":
    app.run(debug=True)