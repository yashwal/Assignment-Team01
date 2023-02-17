import sys
sys.path.append('..')
from database.connection import *

def all_products():
    res=connectDB()
    conn=res[0]
    cur=res[1]
    cur.execute("select product_id,title,price,description,parent_id,cat_label from product INNER JOIN category02 on product.cat_id=category02.cat_id ")
    data=cur.fetchall()
    return data