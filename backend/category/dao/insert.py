import sys
sys.path.append('..')
from database.connection import *

def category_insertion(data):

    '''
    creates category table in PostgreSQL with columns cat_id,cat_label and parent_id. cat_id is the primary key.
    Populates the databse with cat_id,cat_label and parent_id.
    cat_label is the name of categorylevel1 and parent_is is the mapping between categorylevel1 and its parent category.
    '''

    res=connectDB()
    conn=res[0]
    cur=res[1]
    
    cur.execute("create table category(cat_id text PRIMARY key,cat_label text,parent_id text)")

    mapp = {}
    count = 0

    for product in data:
        catLevel1=str(product['catlevel1Name'])
        if catLevel1 not in mapp:
            mapp[catLevel1] = count
            count += 1
    
    for cat1 in mapp:
        cur.execute("INSERT INTO category values(%s,%s,%s)",(mapp[cat1],cat1,-1))
        conn.commit()
    
    for product in data:
        catLevel1=str(product['catlevel1Name'])
        try:
            catLevel2=str(product['catlevel2Name']).replace(" ",'')
            catLevel2=catLevel2.replace("&",'')
        except:
            catLevel2 = "Others"
        parent_id = mapp[catLevel1]

        cur.execute("INSERT INTO category values(%s,%s,%s)",(count,catLevel2,str(parent_id),))       
        count+=1
        conn.commit()
        
    return{"Status":"200"}