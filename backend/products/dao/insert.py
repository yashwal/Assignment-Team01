import sys
sys.path.append('..')
from database.connection import *
import random



def product_insert(data):
    '''
    creates a table named product which has all the product details
    A JSON file is given as input
    the function connects to the database and adds data to the product table
    '''
    res=connectDB() #establish connection with database
    conn=res[0]
    cur=res[1]
    
    cur.execute("create table product(product_id text PRIMARY key,title text,description text,image_url text,price text,cat_id varchar,rating float)")
    #creating product table in sql
    
    mapp = {}
    count = 0
    cur.execute("select cat_id,cat_label,parent_id from category02")
    category=cur.fetchall()

    for product in data:
        catLevel1=str(product['catlevel1Name'])
        if catLevel1 not in mapp:
            mapp[catLevel1] = count
            count += 1
    
    for product in data:
        product_id=str(product['uniqueId'])
        title=str(product['title'])
        try:
            description=(product['productDescription'])
        except:
            description=""
            print("0")
        image_url=str(product['productImage'])
        price=str(product['price'])
        catLevel1=str(product['catlevel1Name'])
        try:
            catLevel2=str(product['catlevel2Name']).replace(" ",'')
            catLevel2=catLevel2.replace("&",'')
        except:
            catLevel2 = "Others"

        cat_id=""

        for temp in category:
            if(temp[1]==catLevel2 and temp[2]==str(mapp[catLevel1])):
                cat_id=temp[0]

        rating_list=[2.0,2.5,3.0,3.5,4.0,4.5,5]
        rating = random.choice(rating_list)

        cur.execute("INSERT INTO product values(%s,%s,%s,%s,%s,%s,%s)",(product_id.strip(),title.strip(),description.strip(),image_url.strip(),price,cat_id,rating))
        #inserting data into product table
        count+=1
        conn.commit()
        
    return{"Product and Category Table population":"Successfull","Status":200}