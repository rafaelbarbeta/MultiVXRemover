import sqlite3
import os

def create_sqlite_db():
    conn = sqlite3.connect('hashDB.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE hashDB
                 (hash_text)''')
    return conn

def insert_hash(hash_text,conn):
    """Insert hash into hashDB"""
    conn.execute("INSERT INTO hashDB VALUES (?)", (hash_text,))

def parse_hash_file(file_path,conn):
    """Parse hash file and insert into hashDB"""
    with open(file_path, "r") as f:
        for line in f.readlines()[6:]:
            insert_hash(line.strip(),conn)

conn = create_sqlite_db()
filenames = os.listdir(os.path.join(os.getcwd(),"VirusShareHashes"))
filenames.sort()
for filename in filenames:
    if filename.endswith(".md5"):
        print(f"Adding {filename} into hashDB")
        parse_hash_file(os.path.join(os.getcwd(),"VirusShareHashes",filename),conn)
        conn.commit()
conn.close()