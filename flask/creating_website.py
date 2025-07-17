from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'aravind26'
app.config['MYSQL_DB'] = 'portfolio'

mysql = MySQL(app)

def init_db():
    cursor = mysql.connection.cursor()
    
    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects1 (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100),
            description TEXT
        )
    """)
    
    # Optional: Clear existing records to avoid duplicates
    cursor.execute("DELETE FROM projects")
    
    # Insert sample data
    cursor.execute("""
        INSERT INTO projects (name, description) VALUES
        ('Portfolio Website', 'My personal portfolio website built with Flask'),
        ('Blog App', 'A simple blog application'),
        ('To-Do App', 'A task management app')
    """)
    
    mysql.connection.commit()
    cursor.close()

@app.route('/')
def home():
    return render_template("homepage.html")

@app.route('/about')
def about():
    return render_template("aboutpage.html")

@app.route('/projects')
def projects():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    cursor.close()
    return render_template("projectspage.html", projects=projects)

if __name__ == "__main__":
    with app.app_context():
        init_db()  # Initialize DB (create table + insert data)
    app.run(debug=True, port=1234)
