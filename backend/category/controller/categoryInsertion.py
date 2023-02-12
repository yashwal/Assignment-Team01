import sys
sys.path.append('..')
from category.dao.insert import *

def categoryTable(data):
    '''
    creates category table in PostgreSQL with columns cat_id,cat_label and parent_id. cat_id is the primary key.
    Populates the databse with cat_id,cat_label and parent_id.
    cat_label is the name of categorylevel1 and parent_is is the mapping between categorylevel1 and its parent category.
    '''
    
    return category_insertion(data)
    
    
    