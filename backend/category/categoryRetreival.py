import sys
sys.path.append('..')
from database.Connection import *
import requests,json

def searchProducts(catLevel1,catLevel2):
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
    cur.close()
    conn.close()
    return data

def categoryLevel():
    '''
    Access the category table and creates the category tree in the form of list of lists.
    the first list contains all categorylevel1 items and second list contains all categorylevel2 items.
    '''
    res=connectDB()
    conn=res[0]
    cur=res[1]
    cur.execute("select distinct cat_label,cat_id from category where parent_id='-1'")
    data=cur.fetchall()
    new_data = []
    cat1=[]
    men=[]
    women=[]
    
    for catlevel1 in data:
        cat1.append([catlevel1[0],catlevel1[1]])

    cur.execute("select distinct cat_label from category where parent_id='0'")
    data=cur.fetchall()
    for catlevel2 in data:
        men.append(catlevel2[0])
    
    cur.execute("select distinct cat_label from category where parent_id='1'")
    data=cur.fetchall()
    for catlevel2 in data:
        women.append(catlevel2[0])
    new_data.append(cat1)
    new_data.append({"0":men})
    new_data.append({"1":women})
    cur.close()
    conn.close()
    return new_data



