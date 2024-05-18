import mysql.connector
# import openpyxl
import xlrd
from flask import Flask

app = Flask(__name__)

# Replace with your MySQL database credentials
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Student_Data"
)
# Create a cursor to execute SQL queries
cursor = db_connection.cursor()
# db_creation_query="""
# create database Student_Data
# """
# cursor.execute(db_creation_query)
# db_connection.commit()
# create_table_query = """
# CREATE TABLE student_performence(
#     Roll_Number INT AUTO_INCREMENT PRIMARY KEY,
#     Name VARCHAR(50),
#     Percentage INT,
#     Grade VARCHAR(5)
# )
# """
# cursor.execute(create_table_query)
# db_connection.commit()

excel_sheet=xlrd.open_workbook('D:\Projects.xlsx')
sheet_name=excel_sheet.sheet_names()

insert_data_query = """
INSERT INTO student_performence (Roll_Number, Name,Percentage,Grade) VALUES (%s, %s, %s, %s)
"""
#data_to_insert = (25,"Virush",80,"A")
# data_to_insert=(35,"Adarsh",60,'B')
# cursor.execute(insert_data_query, data_to_insert)
# db_connection.commit()

for sh in range(0,len(sheet_name)):
    sheet=excel_sheet.sheet_by_index(sh)

    for r in range(1,sheet.nrows):
        Roll_Number=sheet.cell(r,0).value
        Name=sheet.cell(r,1).value
        Percentage=sheet.cell(r,2).value
        Grade=sheet.cell(r,3).value
        student_values=(Roll_Number,Name,Percentage,Grade)
        cursor.execute(insert_data_query, student_values)
        db_connection.commit()
#         #cursor.close()
#         #db_connection.close()



# select_query="""
# select * from student_performence
# """
# cursor.execute(select_query)
# records = cursor.fetchall()
# print(records)
# update_data_query = """
# UPDATE student_performence SET percentage = %s WHERE Name = %s
# """
# new_percentage = 90
# name_to_update = "Virush"
# cursor.execute(update_data_query, (new_percentage, name_to_update))
# db_connection.commit()
# delete_data_query = """
# DELETE FROM student_performence WHERE roll_number = %s
# """
# name_to_delete = 10
# cursor.execute(delete_data_query, (name_to_delete,))
# db_connection.commit()