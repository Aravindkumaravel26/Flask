from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'aravind26'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route("/")
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  user, phone FROM branch1")
    users = cursor.fetchall()
    cursor.close()
    return render_template("index1.html", users=users)

# Add user
@app.route("/add_user", methods=["POST"])
def add_user():
    user = request.form["user"]
    phone = request.form["phone"]
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO branch1 (user, phone) VALUES (%s, %s)", (user, phone))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)