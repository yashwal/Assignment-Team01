from dbConnection import *

def uploadCategory(data):
    res=connectDB()
    conn=res[0]
    cur=res[1]
    #cur.execute("create table category03(cat_id text PRIMARY key,cat_label text,parent_id text)")
    #cur.execute("create table product02(product_id text PRIMARY key,title text,description text,image_url text,price text,cat_id text)")
    mapp = {}
    count = 0

    for i in data:
        catLevel1=str(i['catlevel1Name'])
        if catLevel1 not in mapp:
            mapp[catLevel1] = count
            count += 1
    
    for i in mapp:
        cur.execute("INSERT INTO category03 values(%s,%s,%s)",(mapp[i],i,0))
        conn.commit()
    
    for i in data:
        product_id=str(i['uniqueId'])
        title=(i['title'])
        try:
            description=(i['productDescription'])
        except:
            description=""
            print("0")
        image_url=str(i['productImage'])
        price=str(i['price'])
        catLevel1=str(i['catlevel1Name'])
        try:
            catLevel2=str(i['catlevel2Name'])
        except:
            catLevel2 = "Others"
        parent_id = mapp[catLevel1]
        cur.execute("INSERT INTO category03 values(%s,%s,%s)",(count,catLevel2,str(parent_id),))
        cur.execute("INSERT INTO product02 values(%s,%s,%s,%s,%s,%s)",(product_id,title,description,image_url,price,count))
        count+=1
        conn.commit()

    print("Sucessfully added data to category database")
    return{"Status":200}






# def uploadProduct(data):
#     cur.execute("create table product02(product_id text PRIMARY key,title text,description text,image_url text,price text,cat_id text)")
#     for i in data:
#         product_id=str(i['uniqueId'])
#         title=(i['title'])
#         try:
#             description=(i['productDescription'])
#         except:
#             description=""
#             print("0")
#         image_url=str(i['productImage'])
#         price=str(i['price'])
        
#         cur.execute("INSERT INTO product values(%s,%s,%s,%s,%s)",(product_id,title,description,image_url,price, ))
#         conn.commit()

#     print("Sucessfully added data to product database")
#     return{"Status":200}




