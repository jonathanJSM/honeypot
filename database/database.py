# database.py
import sqlite3

def create_database():
    conn = sqlite3.connect('honeypot.db')
    cursor = conn.cursor()

    # Create a table to store attack data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attacks (
            id INTEGER PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            source_ip TEXT,
            attack_type TEXT,
            data TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insert_attack(source_ip, attack_type, data):
    conn = sqlite3.connect('honeypot.db')
    cursor = conn.cursor()

    # Insert attack data into the database
    cursor.execute('''
        INSERT INTO attacks (source_ip, attack_type, data)
        VALUES (?, ?, ?)
    ''', (source_ip, attack_type, data))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
