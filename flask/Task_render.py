from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')

def home():
    return render_template('T_home.html')

@app.route('/about')
def about():
    return render_template('T_about.html')

@app.route('/contact')
def contact():
    return render_template('T_contact.html')

if __name__ == "__main__":
    app.run(debug=True)