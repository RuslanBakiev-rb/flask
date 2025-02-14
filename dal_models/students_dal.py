from connection_db import connection_db
import psycopg2

class StudentsDAL(object):
    @staticmethod
    def get_all_students():
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = 'SELECT * FROM students'
                cursor.execute(query)
                fetch = cursor.fetchall()
                return fetch
        except Exception as error:
            print(str(error))
        finally:
            conn.close()

    def insert_students():
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                insert_students = '''INSERT INTO students (id, first_name, last_name, group_students)'
                                   'VALUES (%s, %s, %s, %s)'''

                insert_values = [(8, 'Rulon', 'Oboev', '8432-88'), (9, 'Ebal', 'Alabaev', '8432-88'), (10, 'Polet', 'Samoletov', '3231-13')]
                cursor.execute(insert_students, insert_values)
                conn.commit()
            return True
        except Exception as error:
            print(str(error))
        finally:
            conn.close()

