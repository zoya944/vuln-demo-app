from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER, name TEXT, email TEXT)")
    conn.execute("INSERT INTO users VALUES (1, 'Ali', 'ali@example.com')")
    conn.execute("INSERT INTO users VALUES (2, 'Sara', 'sara@example.com')")
    return conn

@app.route("/")
def home():
    return "<h1>Demo App</h1><p>Try /user?name=Ali</p>"

@app.route("/user")
def get_user():
    name = request.args.get("name", "")
    conn = get_db()
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    result = conn.execute(query).fetchall()
    return {"results": result}

app.secret_key = "12345"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)