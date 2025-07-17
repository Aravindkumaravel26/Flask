from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('homeinherit.html')

@app.route('/about')
def about():
    return render_template('aboutinherit.html')

@app.route('/content')
def content():
    return render_template('contentinherit.html')

if __name__=='__main__':
    app.run(debug=True)