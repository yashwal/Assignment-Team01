import sys
sys.path.append('..')
from database.Connection import *
import requests,json

def getProducts(productId):
    ''''
    The databse is searched for the given productId, if found, will return all the product details.
    If not found, a search request is sent to unbxd search api and the required details are fetched. 
    
    '''
    
    res=connectDB()
    conn=res[0]
    cur=res[1]
    cur.execute("select * from product where product_id=%s",(str(productId),))
    data=cur.fetchone()
    if(data == None):
        unbxdApi = f"https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?q={productId}&fields=productDescription,name,price,productImage"
        response=requests.get(unbxdApi)
        response = json.loads(response.content)
        print(response['response']['products'])
        return{
        "product_id":productId,
        "title":response['response']['products'][0]['name'],
        "description":response['response']['products'][0]['productDescription'],
        "image_url":response['response']['products'][0]['productImage'],
        "price":response['response']['products'][0]['price']
    }
    cur.close()
    conn.close()
    return{
        "product_id":productId,
        "title":data[1],
        "description":data[2],
        "image_url":data[3],
        "price":data[4]
    }