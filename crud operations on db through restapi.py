import pymysql
from flask import flash, request
from app import app
from db_config import mysql

# print("test")
# conn = mysql.connect()
# cursor = conn.cursor(pymysql.cursors.DictCursor)
# cursor.execute("SELECT * FROM employees")
# result = cursor.fetchall()
# print(result)


# Get all employees
@app.route("/employees", methods=['GET'])
def get_employees():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchall()
    print(result)
    cursor.close()
    return {"employees": result}


#
# # # Get an employee by ID
# @app.route("/employees/<int:id>", methods=['GET'])
# def get_employee(id):
#     conn = mysql.connect()
#     cursor = conn.cursor(pymysql.cursors.DictCursor)
#     cursor.execute("SELECT * FROM employees WHERE id=%s")
#     result = cursor.fetchall()
#     print(result)
#     cursor.close()
#     return {"employees": result}


# # Add a new employee
@app.route("/employees", methods=['POST'])
def add_employee():
    _json = request.json
    _name = _json['name']
    _age = _json['age']
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = "INSERT INTO employees (name, age) VALUES (%s, %s)"
    print(sql)
    val = (_name, _age)
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    return {"message": "Employee added successfully"}


# # Add a new employee
@app.route("/employees", methods=['PUT'])
def update_employee():
    _json = request.json
    _id = _json['id']
    _name = _json['name']
    _age = _json['age']
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = "UPDATE employees SET name=%s, age=%s WHERE id=%s"
    data = (_name, _age, _id)
    print(data)
    cursor.execute(sql, data)
    conn.commit()
    cursor.close()
    return {"message": "Employee Updated successfully"}


# Delete an employee by ID
@app.route("/employees/<int:id>", methods=['DELETE'])
def delete_employee(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM employees WHERE id = {id}")
    conn.commit()
    cursor.close()
    return {"message": "Employee deleted successfully"}


if __name__ == "__main__":
    app.run()
