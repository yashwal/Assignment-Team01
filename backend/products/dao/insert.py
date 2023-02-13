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
    
    cur.execute("create table product(product_id text PRIMARY key,title text,description text,image_url text,price text,cat_id varchar)")
    mapp = {}
    count = 0
    cur.execute("select cat_id,cat_label,parent_id from category02")
    category=cur.fetchall()

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
            print("0")
        image_url=str(i['productImage'])
        price=str(i['price'])
        catLevel1=str(i['catlevel1Name'])
        try:
            catLevel2=str(i['catlevel2Name']).replace(" ",'')
            catLevel2=catLevel2.replace("&",'')
        except:
            catLevel2 = "Others"

        cat_id=""

        for temp in category:
            if(temp[1]==catLevel2 and temp[2]==str(mapp[catLevel1])):
                cat_id=temp[0]
        cur.execute("INSERT INTO product values(%s,%s,%s,%s,%s,%s)",(product_id.strip(),title.strip(),description.strip(),image_url.strip(),price,cat_id))
        count+=1
        conn.commit()
        
    return{"Product and Category Table population":"Successfull","Status":200}