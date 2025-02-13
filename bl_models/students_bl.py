from dal_models.students_dal import StudentsDAL
from connection_db import connection_db

class StudentsBL():
    @staticmethod
    def get_all_students():
        return StudentsDAL.get_all_students()