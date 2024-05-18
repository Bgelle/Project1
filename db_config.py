from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
print("test")
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'mydatabase'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
print("test")
mysql.init_app(app)
print("test")
print(mysql)