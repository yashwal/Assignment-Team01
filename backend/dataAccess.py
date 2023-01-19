import psycopg2

conn = psycopg2.connect(host="localhost", database="unbxd", user="postgres", password="unbxd")
cur=conn.cursor()

def uploadProduct(data):
    #cur.execute("create table product(product_id text PRIMARY key,title text,decription text,image_url text,price text)")
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
        
        cur.execute("INSERT INTO product values(%s,%s,%s,%s,%s)",(product_id,title,description,image_url,price, ))
        conn.commit()
    print("Sucessfully added data to product database")
    return{"Status":200}

def uploadCategory(data):
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
            catLevel2=str(i['catlevel2Name'])
        except:
            catLevel2 = 'Null'
        parent_id = mapp[catLevel1]
        cur.execute("INSERT INTO category02 values(%s,%s,%s)",(product_id,catLevel2,str(parent_id),))
        conn.commit()

    print("Sucessfully added data to category database")
    return{"Status":200}

def getProducts(productId):
    cur.execute("select * from product where product_id=%s",(str(productId),))
    data=cur.fetchone()
    return{
        "product_id":productId,
        "title":data[1],
        "description":data[2],
        "image_url":data[3],
        "price":data[4]
    }

def checkProductID(productId):
    cur.execute("select * from product where product_id=%s",(productId,))
    data= cur.fetchone()
    if(data==None):
        return 0
    return 1


def updateDB(newTitle,newDesc,newUrl,newPrice,productId):
    cur.execute("update product set title = %s,decription = %s,image_url = %s,price = %s where product_id=%s",(str(newTitle),str(newDesc),str(newUrl),str(newPrice),productId,))
    conn.commit()
    print({"Message":"DB updated"})
    return 1



def updateTitle(newTitle,productId):
    cur.execute("update product set title = %s where product_id=%s",(str(newTitle),productId,))
    conn.commit()
    print({"Message":"Title updated"})
    return 1

def updateDesc(newDesc,productId):
    cur.execute("update product set decription = %s where product_id=%s",(str(newDesc),productId,))
    conn.commit()
    print({"Message":"Description updated"})
    return 1


def updateUrl(newUrl,productId):
    cur.execute("update product set image_url = %s where product_id=%s",(str(newUrl),productId,))
    conn.commit()
    print({"Message":"URL updated"})
    return 1


def updatePrice(newPrice,productId):
    cur.execute("update product set price = %s where product_id=%s",(str(newPrice),productId,))
    conn.commit()
    print({"Message":"Price updated"})
    return 1










