import sys
sys.path.append('..')
from database.Connection import *



def categoryTable(data):
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

    for i in data:
        catLevel1=str(i['catlevel1Name'])
        if catLevel1 not in mapp:
            mapp[catLevel1] = count
            count += 1
    
    for i in mapp:
        cur.execute("INSERT INTO category values(%s,%s,%s)",(mapp[i],i,-1))
        conn.commit()
    
    for i in data:
        catLevel1=str(i['catlevel1Name'])
        try:
            catLevel2=str(i['catlevel2Name']).replace(" ",'')
            catLevel2=catLevel2.replace("&",'')
        except:
            catLevel2 = "Others"
        parent_id = mapp[catLevel1]
        cur.execute("INSERT INTO category values(%s,%s,%s)",(count,catLevel2,str(parent_id),))
        count+=1
        conn.commit()

    print("Sucessfully added data to category database")
    return{"Status":200}