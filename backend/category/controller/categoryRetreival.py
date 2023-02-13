import sys
sys.path.append('..')
from flask import request
from category.dao.retreive import *
from category.dao.tree import *


def searchCategory(catId):
    '''
    category level 1 and 2 are given as input along with pagenumber and sort key
    returns products list
    '''
    pageNumber = request.args.get('page', default=1, type=int)
    sortKey = request.args.get('sort', default="ftrd", type =str)
    pageNumber=(pageNumber-1)*9
    
    return retrieve_category(catId,pageNumber,sortKey)

    

def categoryLevel():
    '''
    accesses category table and then returns category tree.
    '''
    return category_tree()