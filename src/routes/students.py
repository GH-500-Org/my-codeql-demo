from flask import Blueprint, jsonify, request

from services.student_service import (
    get_all_students,
    get_student_by_id,
    create_student,
    update_student,
    delete_student,
)

students_bp = Blueprint("students", __name__)


@students_bp.route("/students", methods=["GET"])
def list_students():
    return jsonify(get_all_students())


@students_bp.route("/students/<id>", methods=["GET"])
def get_student(id):
    student = get_student_by_id(id)
    return jsonify(student)


@students_bp.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    student = create_student(data)
    return jsonify(student), 201


@students_bp.route("/students/<id>", methods=["PUT"])
def edit_student(id):
    data = request.get_json()
    student = update_student(id, data)
    return jsonify(student)


@students_bp.route("/students/<id>", methods=["DELETE"])
def remove_student(id):
    student = delete_student(id)
    return jsonify(student)
