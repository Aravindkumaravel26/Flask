from flask import Flask, render_template,redirect,url_for
req = Flask(__name__)
@req.route('/')

def dt():
    a = "Welcome To GBU World Mame!"
    return a

@req.route('/home')
def home():
    return render_template('filter.html', b = "Hii...Friends Iam Aravind!")

@req.route('/about')
def againhome():
    return redirect('/home')

@req.route('/visit')
def agnhome():
    return redirect(url_for("dt"))

@req.route('/css')
def htl():
    return render_template('html_css.html')

if __name__ == "__main__":
    req.run(debug=True)