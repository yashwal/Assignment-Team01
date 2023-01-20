from dbConnection import *


def checkProductID(productId):
    res=connectDB()
    conn=res[0]
    cur=res[1]
    cur.execute("select * from product where product_id=%s",(productId,))
    data= cur.fetchone()
    cur.close()
    conn.close()
    if(data==None):
        return 0
    return 1
    


def updateDB(newTitle,newDesc,newUrl,newPrice,productId):
    res=connectDB()
    conn=res[0]
    cur=res[1]
    cur.execute("update product set title = %s,description = %s,image_url = %s,price = %s where product_id=%s",(str(newTitle),str(newDesc),str(newUrl),newPrice,productId,))
    conn.commit()
    cur.close()
    conn.close()
    print({"Message":"DB updated"})
    return {"status":200}
    






'''
#future work
def updateTitle(newTitle,productId):
    cur.execute("update product set title = %s where product_id=%s",(str(newTitle),productId,))
    conn.commit()
    print({"Message":"Title updated"})
    return 1

def updateDesc(newDesc,productId):
    cur.execute("update product set decription = %s where product_id=%s",(str(newDesc),productId,))
    conn.commit()
    print({"Message":"Description updated"})
    return 1


def updateUrl(newUrl,productId):
    cur.execute("update product set image_url = %s where product_id=%s",(str(newUrl),productId,))
    conn.commit()
    print({"Message":"URL updated"})
    return 1


def updatePrice(newPrice,productId):
    cur.execute("update product set price = %s where product_id=%s",(str(newPrice),productId,))
    conn.commit()
    print({"Message":"Price updated"})
    return 1

'''