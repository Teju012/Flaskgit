from flask import Flask,render_template
app=Flask(__name__)
@app.route('/<name>')
def fun(name):
    return render_template("mood.html", name=name)
app.run()