import sqlite3


def create_connection():
    conn = sqlite3.connect("database.db")
    return conn


def create_table():
    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        dob TEXT NOT NULL,
        email TEXT NOT NULL,
        glucose REAL NOT NULL,
        haemoglobin REAL NOT NULL,
        cholesterol REAL NOT NULL,
        prediction TEXT
    )
    """)

    conn.commit()
    conn.close()
def add_patient(full_name, dob, email, glucose, haemoglobin, cholesterol, prediction):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO patients (
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        prediction
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        prediction
    ))

    conn.commit()
    conn.close()   
def get_all_patients():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")

    patients = cursor.fetchall()

    conn.close()

    return patients    
def update_patient(id, full_name, dob, email, glucose, haemoglobin, cholesterol):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE patients
    SET
        full_name = ?,
        dob = ?,
        email = ?,
        glucose = ?,
        haemoglobin = ?,
        cholesterol = ?
    WHERE id = ?
    """, (
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        id
    ))

    conn.commit()
    conn.close()
def delete_patient(id):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM patients WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()    