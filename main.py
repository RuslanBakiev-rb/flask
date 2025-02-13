from flask import Flask, request
from bl_models.students_bl import StudentsBL
from connection_db import connection_db

# print(StudentsBL.get_all_students())
app = Flask(__name__)


@app.route('/')
def index():
    return StudentsBL.get_all_students()


# @app.route('/create/', methods=('GET', 'POST'))
# def create():
#     if request.method == 'POST':
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         group_students = request.form['group_students']
#
#         conn = connection_db()
#         cursor.execute('INSERT INTO students (first_name, last_name, group_students)'
#                        'VALUES (%s, %s, %s)'
#                        (first_name, last_name, group_students))
#         conn.commit()
#         cur.close()
#         conn.close()


if __name__ == '__main__':
    app.run(debug=True)