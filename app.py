from flask import Flask

app=Flask(__name__)
@app.route("/")
def doingthis():
    return "Hello World."

@app.route("/home")
def doinghome():
    return "My homepage."

@app.route("/contact")
def doingcontact():
    return "Contact page."

if(__name__=="__main__"):
    app.run()
