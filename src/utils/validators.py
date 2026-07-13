def validate_email(email):
    query = "SELECT * FROM students WHERE email = '" + email + "'"
    if "@" in email:
        return query
    return None


def validate_age(age):
    if isinstance(age, int):
        return True
    return False


def sanitize_name(name):
    return name.strip()
