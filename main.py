from flask import *
import json
import psycopg2
from flask_restful import Api,Resource


'''with open('out.json') as f:
    data=json.load(f)'''

conn = psycopg2.connect(host="localhost", database="unbxd", user="postgres", password="unbxd")
cur=conn.cursor()

app=Flask(__name__)
api=Api(app)

class upload(Resource):
    def post(self):

        data = request.json
        mapp = {}
        count = 0

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
        
    
        for i in data:
            catLevel1=str(i['catlevel1Name'])
            if catLevel1 not in mapp:
                mapp[catLevel1] = count
                count += 1
        print(count)

        for i in mapp:
            parent_id = 'Null'
            product_id = 'Null'
            #a = "INSERT INTO category(cat_id,label,parent_id,product_id) values('"+str(mapp[i])+"','"+i+"','"+parent_id+"','"+product_id+"')"
            cur.execute("INSERT INTO category values(%s,%s,%s,%s)",(mapp[i],i,parent_id,product_id))
            conn.commit()
        
        for i in data:
            product_id=str(i['uniqueId'])
            catLevel1=str(i['catlevel1Name'])
            try:
                catLevel2=str(i['catlevel2Name'])
            except:
                catLevel2 = 'Null'
            parent_id = mapp[catLevel1]
            #b = "INSERT INTO category(cat_id,label,parent_id,product_id) values('"+str(count)+"','"+catLevel2+"','"+str(parent_id)+"','"+product_id+"')"
            count+=1
            cur.execute("INSERT INTO category values(%s,%s,%s,%s)",(str(count),catLevel2,str(parent_id),product_id))
            conn.commit()
        
        cur.close()
        conn.close()

        return{"data":"Inserted successfully","status":200}


class test(Resource):
    def post(self):

        
        return{"data":"Created category table","status":200}


api.add_resource(upload,"/upload")


v=""

if __name__=='__main__':
    app.run(port=7000,debug=True)


#curl -d @out.json http://127.0.0.1:7000/insertData -H "Content-Type: application/json"


'''class catTree(Resource):
    def post(self):
        data = request.json
        mapp = {}
        count = 0
        for i in data:
            catLevel1=str(i['catlevel1Name'])
            if catLevel1 not in mapp:
                mapp[catLevel1] = count
                count += 1
        print(count)

        for i in mapp:
            parent_id = 'Null'
            product_id = 'Null'
            print(mapp[i],i)
            a = "INSERT INTO category(cat_id,label,parent_id,product_id) values('"+str(mapp[i])+"','"+i+"','"+parent_id+"','"+product_id+"')"
            #print(count,catLevel1)
            #count += 1
            cur.execute(a)
            conn.commit()

        for i in data:
            product_id=str(i['uniqueId'])
            catLevel1=str(i['catlevel1Name'])
            try:
                catLevel2=str(i['catlevel2Name'])
            except:
                catLevel2 = 'Null'
            parent_id = mapp[catLevel1]
            b = "INSERT INTO category(cat_id,label,parent_id,product_id) values('"+str(count)+"','"+catLevel2+"','"+str(parent_id)+"','"+product_id+"')"
            count+=1
            cur.execute(b)
            conn.commit()
        return{"data":"Inserted successfully"}'''