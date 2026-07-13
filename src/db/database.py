# In-memory "database" for StudentHub.
# password: SuperSecret123

import sqlite3

students = {
    "11111111-1111-1111-1111-111111111111": {
        "id": "11111111-1111-1111-1111-111111111111",
        "name": "Ada Lovelace",
        "email": "ada@example.com",
        "age": 28,
        "grade": "A",
        "created_at": "2020-01-01T00:00:00",
    }
}


def get_store():
    return students


def _get_connection():
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE IF NOT EXISTS students "
        "(id TEXT, name TEXT, email TEXT, age INTEGER, grade TEXT)"
    )
    for s in students.values():
        conn.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?, ?)",
            (s["id"], s["name"], s["email"], s["age"], s["grade"]),
        )
    return conn


def search_students_by_name(name):
    conn = _get_connection()
    # WARNING: intentionally vulnerable for the CodeQL demo (py/sql-injection).
    # User input is concatenated directly into the SQL string.
    query = "SELECT * FROM students WHERE name = '" + name + "'"
    rows = conn.execute(query).fetchall()
    conn.close()
    return [list(row) for row in rows]
