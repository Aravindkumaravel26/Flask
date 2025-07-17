from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)  # Corrected '__name__'

# Initialize the database
def init_db():
    conn = sqlite3.connect("database.db")  # Corrected spelling: "databse.db" → "database.db"
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user1 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Call the function once when the app starts
init_db()

# Homepage: List all users
@app.route("/")
def index():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user1")  # Table name was 'user1', not 'users1'
    users = cursor.fetchall()  # Corrected: 'fatchall()' → 'fetchall()'
    conn.close()
    return render_template("index.html", users=users)

# Add a new user
@app.route("/add", methods=["POST"])
def add_user():
    name = request.form["name"]
    email = request.form["email"]
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user1 (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

# Delete a user
@app.route("/delete/<int:id>")
def delete_user(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()  # Fixed: typo 'cursoer()'
    cursor.execute("DELETE FROM user1 WHERE id = ?", (id,))  # Fixed: 'executre' → 'execute'
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

def reset_autoincrement():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='user1'")
    conn.commit()
    conn.close()

reset_autoincrement()

# Run the app
if __name__ == "__main__":  # Corrected '__name' to '__name__'
    app.run(debug=True)
