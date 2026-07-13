from dataclasses import dataclass


@dataclass
class Student:
    id: str
    name: str
    email: str
    age: int
    grade: str
    created_at: str
