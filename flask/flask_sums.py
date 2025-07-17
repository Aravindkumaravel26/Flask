from flask import Flask,request
app = Flask(__name__)
@app.route("/")

def home():
    return "Welcome to the Flask World!"

@app.route("/about")
def about():
    return "This is a About Page!"

@app.route("/contact")
def contact():
    return "Contact us at: Contact@example.com!"

@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}!"

@app.route("/square/<int:num>")
def square(num):
    return f"Square of {num} is {num**2}"

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        return "Login is successful!"
    return "Please Submit Login Detail's!"

@app.errorhandler(404)
def page_not_found(error):
    return "Oop's! page not found...", 404



if __name__ == "__main__":
    app.run(debug=True,port=1234)