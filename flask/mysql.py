from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'aravind26'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route("/")
def main():
    cursor = mysql.connection.cursor()
    
    cursor.execute("DELETE FROM branch1")
    cursor.execute('''INSERT INTO branch1(user, phone) VALUES("Aravind", "6369051128")''')
    cursor.execute('''INSERT INTO branch1(user, phone) VALUES("Ravi", "12345678")''')
    cursor.execute('''INSERT INTO branch1(user, phone) VALUES("Karthick", "87654321")''')
    cursor.execute('''INSERT INTO branch1(user, phone) VALUES("Vichu", "87654321")''')
    cursor.execute('''INSERT INTO branch1(user, phone) VALUES("Mohideen", "87654321")''')

    # Fetch data
    cursor.execute('''SELECT * FROM branch1''')
    users = cursor.fetchall()

    mysql.connection.commit()
    cursor.close()

    return render_template('index1.html', users=users)

if __name__ == "__main__":
    app.run(debug=True, port=1111)
