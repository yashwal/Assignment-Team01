import sys
sys.path.append('..')
from products.dao.insert import *


def productTable(data):
    '''
    Gets the catalog of products in JSON format.
    Adds the product details into product table by using product_insert function.
    '''
    
    res=product_insert(data)
    if(res["Status"]==200):
        return ("Data inserted to Database Successfully")
    else:
        return ("Retry Data Ingestion on product table")
    







