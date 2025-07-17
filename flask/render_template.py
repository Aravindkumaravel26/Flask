from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")

def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

# Passing data to html template....

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", username=name)



if __name__ == "__main__":
    app.run(debug=True)