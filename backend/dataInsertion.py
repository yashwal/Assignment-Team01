from dbConnection import *

#creates a table named product which has all the product details
#A JSON file is given as input
#the function connects to the database and adds data to the product table
def uploadProduct(data):
    res=connectDB()
    conn=res[0]
    cur=res[1]
    #cur.execute("create table product(product_id text PRIMARY key,title text,description text,image_url text,price text)")
    for i in data:
        product_id=str(i['uniqueId'])
        title=str(i['title'])
        try:
            description=str(i['productDescription'])
        except:
            description=""
            print("0")
        image_url=str(i['productImage'])
        price=(i['price'])
        
        cur.execute("INSERT INTO product values(%s,%s,%s,%s,%s)",(product_id.strip(),title.strip(),description.strip(),image_url.strip(),price, ))
        conn.commit()

    cur.close()
    conn.close()
    print("Sucessfully added data to product database")
    return{"Status":200}



#creates a table category which has product_id, category name and parent_id
#the database connection is initiated 
#data is added into the category table
def uploadCategory(data):
    res=connectDB()
    conn=res[0]
    cur=res[1]

    #cur.execute("create table category01(cat_id text PRIMARY key,label text)")
    #cur.execute("create table category02(product_id text PRIMARY key,cat_label text,parent_id text)")
    mapp = {}
    count = 0

    for i in data:
        catLevel1=str(i['catlevel1Name'])
        if catLevel1 not in mapp:
            mapp[catLevel1] = count
            count += 1
    
    for i in mapp:
        cur.execute("INSERT INTO category01 values(%s,%s)",(mapp[i],i,))
        conn.commit()
    
    for i in data:
        product_id=str(i['uniqueId'])
        catLevel1=str(i['catlevel1Name'])
        try:
            catLevel2=str(i['catlevel2Name']).replace(" ",'')
            catLevel2=catLevel2.replace("&",'')
        except:
            catLevel2 = "Others"
        parent_id = mapp[catLevel1]
        cur.execute("INSERT INTO category02 values(%s,%s,%s)",(product_id,catLevel2,str(parent_id),))
        conn.commit()

    cur.close()
    conn.close()

    print("Sucessfully added data to category database")
    return{"Status":200}

