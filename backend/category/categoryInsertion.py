import sys
sys.path.append('..')
from database.Connection import *

def categoryTable(data):
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
        cur.execute("INSERT INTO category values(%s,%s,%s)",(mapp[i],i,0))
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