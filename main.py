from flask import *
import json,time
import psycopg2

#load JSON file
with open('out.json') as f:
    data=json.load(f)

#connect to postgreSQL database
conn = psycopg2.connect(host="localhost", database="unbxd", user="postgres", password="unbxd")

#create a cursor
cur=conn.cursor()

app=Flask(__name__)

@app.route('/data_ingestion',methods=['GET'])
def data_ingestion():
    for i in data:
        product_id=str(i['uniqueId'])
        try:
            title=str(i['title'])
            title=title.replace("'","`")

        except:
            print("0")

        try:
            decription=(i["productDescription"])
        except:
            print("0")
        decription=decription.replace("'","`")
        image_url=str(i['productImage'])
        price=str(i['price'])
        catLevel1=str(i['catlevel1Name'])
        try:
            catLevel2=str(i['catlevel2Name'])
        except:
            print("0")
        #print(i)
        a="INSERT INTO product(product_id,title,decription,image_url,price,catlevel1,catlevel2) values('"+product_id+"','"+title+"','"+decription+"','"+image_url+"','"+price+"','"+catLevel1+"','"+catLevel1+"')"
        #print(a)
        cur.execute(a)
        conn.commit()

    #close connection and cursor
    cur.close()
    conn.close()
    
if(__name__)== '__main__':
    app.run(port=7000)
