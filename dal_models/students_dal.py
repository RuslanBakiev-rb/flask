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