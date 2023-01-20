from dbConnection import *


def getProducts(productId):
    res=connectDB()
    conn=res[0]
    cur=res[1]
    cur.execute("select * from product where product_id=%s",(str(productId),))
    data=cur.fetchone()
    cur.close()
    conn.close()
    return{
        "product_id":productId,
        "title":data[1],
        "description":data[2],
        "image_url":data[3],
        "price":data[4]
    }

def getCategory(catLevel1,catLevel2):
    res=connectDB()
    conn=res[0]
    cur=res[1]
    cur.execute("select product.product_id,title,description,image_url,price from product FULL OUTER JOIN category02 on product.product_id = category02.product_id where parent_id=%s AND cat_label=%s ",(catLevel1,catLevel2))
    data=cur.fetchall()
    cur.close()
    conn.close()
    return data



