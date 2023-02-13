import requests,json
from flask import request
import logging

def searchProduct(searchQuery):
    '''
    Sends a get request to nbxd search api and returns the response.
    input agruments are search query,page number and sort key.
    '''

    pageNumber = request.args.get('page', default=1, type=int)
    sortKey = request.args.get('sort', default="ftrd", type=str)
    pageNumber=(pageNumber-1)*9
    
    if sortKey=='ftrd':
        sortKey=""
        
    unbxdApi = f"https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?q={searchQuery}&rows=9&start={pageNumber}&sort={sortKey}"
    response=requests.get(unbxdApi)
    if response and response.status_code == 200:
        data = json.loads(response.content)
        products = data['response']['products']
        productsNumber = data['response']['numberOfProducts']
        return [productsNumber,products]
    else:
        logging.error("Product search failed")
        return[0,0]


def unbxdSearch(productId) :
    unbxdApi = f"https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?q={productId}&fields=productDescription,name,price,productImage"
    response=requests.get(unbxdApi)
    if response and response.status_code == 200:
        response = json.loads(response.content)
        
        return{
            "product_id":productId,
            "title":response['response']['products'][0]['name'],
            "description":response['response']['products'][0]['productDescription'],
            "image_url":response['response']['products'][0]['productImage'],
            "price":response['response']['products'][0]['price']
        }
    else:
        logging.error("Product search failed ")
        return{}


