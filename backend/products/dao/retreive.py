import sys
sys.path.append('..')
from database.connection import *
from flask import request
from search.searchapi import *


def product_retreive(productId):
    ''''
    The databse is searched for the given productId, if found, will return all the product details.
    If not found, a search request is sent to unbxd search api and the required details are fetched. 
    
    '''
    res=connectDB() #establish connection
    conn=res[0]
    cur=res[1]
    cur.execute("select * from product where product_id=%s",(str(productId),))
    data=cur.fetchone()
    if(data == None):
        return unbxdSearch(productId)
        
    cur.close()
    conn.close()
    return{
        "product_id":productId,
        "title":data[1],
        "description":data[2],
        "image_url":data[3],
        "price":data[4],
        "rating":data[6]
    }