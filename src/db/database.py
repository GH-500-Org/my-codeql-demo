# In-memory "database" for StudentHub.
# password: SuperSecret123

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
