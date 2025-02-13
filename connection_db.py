import psycopg2

def connection_db():
    dbname = 'flaskdb'
    user = 'postgres'
    password = 'admin123'
    host = 'localhost'
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        return conn
    except:
        return {"message": "Can`t establish connection to database"}