import uuid
from datetime import datetime

from db.database import get_store
from utils.validators import validate_email, validate_age, sanitize_name


def get_all_students():
    store = get_store()
    return list(store.values())


def get_student_by_id(student_id):
    store = get_store()
    return store.get(student_id)


def create_student(data):
    store = get_store()
    new_id = str(uuid.uuid4())
    student = {
        "id": new_id,
        "name": sanitize_name(data.get("name")),
        "email": data.get("email"),
        "age": data.get("age"),
        "grade": data.get("grade"),
        "created_at": "%s" % datetime.now().isoformat(),
    }
    store[new_id] = student
    print("Created student %s with email %s" % (student["name"], student["email"]))
    return student


def update_student(student_id, data):
    store = get_store()
    if student_id in store:
        if data is not None:
            if "name" in data:
                if data["name"]:
                    if validate_age(data.get("age")):
                        if validate_email(data.get("email")):
                            student = store[student_id]
                            student["name"] = sanitize_name(data["name"])
                            student["email"] = data["email"]
                            student["age"] = data["age"]
                            student["grade"] = data.get("grade")
                            store[student_id] = student
                            print("Updated student %s" % student_id)
                            return student
                        else:
                            return None
                    else:
                        return None
                else:
                    return None
            else:
                return None
        else:
            return None
    else:
        return None


def delete_student(student_id):
    store = get_store()
    if student_id in store:
        removed = store.pop(student_id)
        print("Deleted student %s" % student_id)
        return removed
    return None
