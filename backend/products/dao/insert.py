import sys
sys.path.append('..')
from database.connection import *



def product_insert(data):
    '''
    creates a table named product which has all the product details
    A JSON file is given as input
    the function connects to the database and adds data to the product table
    '''
    res=connectDB()
    conn=res[0]
    cur=res[1]
    
    try:
        cur.execute("create table product(product_id text PRIMARY key,title text,description text,image_url text,price text,cat_id text)")
    except:
        return {"Status":400}
    mapp = {}
    count = 0

    for i in data:
        catLevel1=str(i['catlevel1Name'])
        if catLevel1 not in mapp:
            mapp[catLevel1] = count
            count += 1
    
    for i in data:
        product_id=str(i['uniqueId'])
        title=str(i['title'])
        try:
            description=(i['productDescription'])
        except:
            description=""
            
        image_url=str(i['productImage'])
        price=str(i['price'])
        try:
            cur.execute("INSERT INTO product values(%s,%s,%s,%s,%s,%s)",(product_id.strip(),title.strip(),description.strip(),image_url.strip(),price,count))
        except:
            return {"Status":400}
        count+=1
        conn.commit()
        
    return{"Status":200}