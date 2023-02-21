import sys
sys.path.append('..')
from database.connection import *
from flask import request


def retrieve_category(catId,pageNumber,sortKey):
    '''
    For given catlevel1 and catlevel2 parameters, the functions fetches the product details from the category and product database.
    '''
    res=connectDB() #establish connection with database
    conn=res[0]
    cur=res[1]
    mapp = {"men":'0',"women":'1',"exp":'2'}
    
    
    #retrieve data from product and category table
    if(catId=="women" or catId=="men" or catId=="exp"):
        cur.execute("select product_id,title,description,image_url,price,rating from product  INNER JOIN category02 on product.cat_id = category02.cat_id where parent_id=%s",(mapp[catId]))
    else:
        cur.execute("select product_id,title,description,image_url,price,rating from product where cat_id=%s",(catId,))
    data=cur.fetchall()

    new_data = []
    for product in data:
        new_data.append({"uniqueId":product[0], "Title":product[1], "Description":product[2],"Img_URL":product[3],"price":product[4],"rating":product[5]})
    
    if(sortKey=="price asc"):
        new_data = sorted(new_data, key=lambda k: float(k['price']))
    if(sortKey=="price desc"):
        new_data = sorted(new_data, key=lambda k: float(k['price']), reverse=True)
    
    if(sortKey=='ftrd'):
        new_data = sorted(new_data, key=lambda k: float(k['rating']), reverse=True)
    sliced_data=new_data[pageNumber:pageNumber+9] 
    
    cur.close()
    conn.close() 
    return [len(new_data),sliced_data]

