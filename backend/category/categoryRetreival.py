import sys
sys.path.append('..')
from database.Connection import *
import requests,json

def searchProducts(catLevel1,catLevel2):
    res=connectDB()
    conn=res[0]
    cur=res[1]
    if(catLevel2=="women" or catLevel2=="men"):
        cur.execute("select product_id,title,description,image_url,price from product  INNER JOIN category on product.cat_id = category.cat_id where parent_id=%s",(catLevel1))
    else:
        cur.execute("select product_id,title,description,image_url,price from product  INNER JOIN category on product.cat_id = category.cat_id where parent_id=%s AND cat_label=%s ",(catLevel1,catLevel2))
    data=cur.fetchall()
    cur.close()
    conn.close()
    return data