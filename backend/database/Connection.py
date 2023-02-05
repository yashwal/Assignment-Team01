import psycopg2

def connectDB():
<<<<<<< HEAD
    conn = psycopg2.connect(host="local-database-1", database="unbxd", user="postgres", password="unbxd")
=======
    '''
    Establishes a connection with unbxd databse with the user as postgres.
    psycopg2 module is used for connection.
    '''
    conn = psycopg2.connect(host="assignment-team01-database-1", database="unbxd", user="postgres", password="unbxd")
>>>>>>> bae6275 (refactor(searchProducts): searchSorted is combined with searchProducts)
    #conn = psycopg2.connect(host="assignment-team01-database-1", database="unbxd", user="postgres", password="unbxd")
    cur=conn.cursor()
    return [conn,cur]

    