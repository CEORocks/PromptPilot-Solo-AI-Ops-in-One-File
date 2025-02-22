import json
import sqlite3
from datetime import datetime

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the User table
cursor.execute('''
CREATE TABLE IF NOT EXISTS User (
    id TEXT PRIMARY KEY,
    name TEXT,
    age INTEGER,
    city TEXT,
    score REAL,
    is_active BOOLEAN,
    status TEXT,
    created_at DATE
)
''')

# Read the JSON file
with open('data/mock.json', 'r') as file:
    users = json.load(file)

# Insert data into the table
for user in users:
    cursor.execute('''
    INSERT INTO User (id, name, age, city, score, is_active, status, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        user['id'],
        user['name'],
        user['age'],
        user['city'],
        user['score'],
        user['is_active'],
        user['status'],
        user['created_at']
    ))

# Commit the changes and close the connection
conn.commit()
conn.close()
