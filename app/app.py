from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

SECRET_KEY = "super-secret-admin-password-123"

@app.route('/')
def home():
    return "Welcome to the Vulnerable DevSecOps Test App!"

@app.route('/search')
def search():
    query = request.args.get('q', '')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    sql = f"SELECT * FROM items WHERE name LIKE '%{query}%'"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except Exception as e:
        results = str(e)
    conn.close()
    return {"results": str(results)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)