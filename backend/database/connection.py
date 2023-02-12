import psycopg2

def connectDB():
    '''
    Establishes a connection with unbxd databse with the user as postgres.
    psycopg2 module is used for connection.
    '''
    #conn = psycopg2.connect(host="local-database-1", database="unbxd", user="postgres", password="unbxd")
    conn = psycopg2.connect(host="assignment-team01-database-1", database="unbxd", user="postgres", password="unbxd")
    cur=conn.cursor()
    return [conn,cur]

    