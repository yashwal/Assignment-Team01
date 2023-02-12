import sys
sys.path.append('..')
from database.connection import *
from products.dao.retreive import *


def getProducts(productId):
    '''
    Returns details of the product by searching in the database.
    If not found in database, unbxd search is queried with product id.
    '''
    return product_retreive(productId)
