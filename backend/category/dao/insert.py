import sys
sys.path.append('..')
from database.connection import *

def category_insertion(data):
    res=connectDB() #establishing connection with database
    conn=res[0]
    cur=res[1]
    
    cur.execute("create table category(cat_id text PRIMARY key,cat_label text,parent_id text)") 
    cur.execute("create table category02(cat_id varchar PRIMARY key,cat_label text,parent_id text)") #Creating category table
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
    
    cur.execute("select distinct cat_label from category where parent_id='0'")
    men=cur.fetchall()

    cur.execute("select distinct cat_label from category where parent_id='1'")
    women=cur.fetchall()

    cur.execute("select distinct cat_label from category where parent_id='2'")
    exp=cur.fetchall()

    id=1
    '''
    inserting details into category02 table
    '''
    for product in men:
        cur.execute("INSERT INTO category02 values(%s,%s,%s)",(id,product[0],"0"))
        id+=1
        conn.commit()
    for product in women:
        cur.execute("INSERT INTO category02 values(%s,%s,%s)",(id,product[0],"1"))
        id+=1
        conn.commit()
    for product in exp:
        cur.execute("INSERT INTO category02 values(%s,%s,%s)",(id,product[0],"2"))
        id+=1
        conn.commit()

        
    return{"Category Table population":"Successfull","Status":200}