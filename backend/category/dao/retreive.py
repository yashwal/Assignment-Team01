import sys
sys.path.append('..')
from database.connection import *
from flask import request


def retrieve_category(catLevel1,catLevel2,pageNumber,sortKey):
    '''
    For given catlevel1 and catlevel2 parameters, the functions fetches the product details from the category and product database.
    '''
    res=connectDB()
    conn=res[0]
    cur=res[1]
    if(catLevel2=="women" or catLevel2=="men"):
        cur.execute("select product_id,title,description,image_url,price from product  INNER JOIN category on product.cat_id = category.cat_id where parent_id=%s",(catLevel1))
    else:
        cur.execute("select product_id,title,description,image_url,price from product  INNER JOIN category on product.cat_id = category.cat_id where parent_id=%s AND cat_label=%s ",(catLevel1,catLevel2))
    data=cur.fetchall()

    new_data = []
    for product in data:
        new_data.append({"uniqueId":product[0], "Title":product[1], "Description":product[2],"Img_URL":product[3],"price":product[4]})
    
    if(sortKey=="price asc"):
        new_data = sorted(new_data, key=lambda k: float(k['price']))
    if(sortKey=="price desc"):
        new_data = sorted(new_data, key=lambda k: float(k['price']), reverse=True)
    
    sliced_data=new_data[pageNumber:pageNumber+9] 
    
    cur.close()
    conn.close()
    return [len(new_data),sliced_data]
