import sys
sys.path.append('..')
from flask import request
from database.connection import *

def category_tree():
    '''
    Access the category table and creates the category tree in the form of list of lists.
    the first list contains all categorylevel1 items and second list contains all categorylevel2 items.
    '''
    res=connectDB() #establish connection with database
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

    cur.execute("select distinct cat_label,cat_id from category02 where parent_id='0'")
    data=cur.fetchall()
    for catlevel2 in data:
        men.append([catlevel2[0],catlevel2[1]])
    
    cur.execute("select distinct cat_label,cat_id  from category02 where parent_id='1'")
    data=cur.fetchall()
    for catlevel2 in data:
        women.append([catlevel2[0],catlevel2[1]])
    new_data.append(cat1)
    new_data.append({"0":men})
    new_data.append({"1":women})
    cur.close()
    conn.close()
    return new_data # return category tree