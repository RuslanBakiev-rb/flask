from flask import Flask, request
from bl_models.students_bl import StudentsBL
from connection_db import connection_db

# print(StudentsBL.get_all_students())
app = Flask(__name__)


@app.route('/')
def index():
    return StudentsBL.get_all_students()


@app.route('/insert', methods=['POST'])
def insert_index():
    return StudentsBL.insert_students()



if __name__ == '__main__':
    app.run(debug=True)