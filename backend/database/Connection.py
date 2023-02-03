import psycopg2

def connectDB():
    conn = psycopg2.connect(host="local-database-1", database="unbxd", user="postgres", password="unbxd")
    #conn = psycopg2.connect(host="assignment-team01-database-1", database="unbxd", user="postgres", password="unbxd")
    cur=conn.cursor()
    return [conn,cur]

    