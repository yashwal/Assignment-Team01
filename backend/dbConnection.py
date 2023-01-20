import psycopg2

def connectDB():
    conn = psycopg2.connect(host="localhost", database="unbxd", user="postgres", password="unbxd")
    cur=conn.cursor()
    return [conn,cur]