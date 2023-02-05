import sys
sys.path.append('..')
from database.Connection import *

#future work

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
    






