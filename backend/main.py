import sys
sys.path.append('..')

from flask import *
from flask_restful import Api,Resource
from flask_cors import CORS
from flask_caching import Cache

from category.categoryInsertion import *
from category.categoryRetreival import *
from product.productInsertion import *
from product.productRetreival import *
from search.searchapi import *
import math
import json


app=Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config.from_object('config.BaseConfig')  # Set the configuration variables to the flask application
cache = Cache(app)
api=Api(app)


#product_id is given as input , returns the product details
class fetchProducts(Resource):
    @cache.cached(timeout=30, query_string=True)
    def get(self,productId):
        #productId = request.args.get('uid', default="", type=str)
        data=getProducts(productId)
        
        return data
api.add_resource(fetchProducts,"/product/<string:productId>")




#upload the given data in the json file to postgreSQL table
class upload(Resource):
    def post(self):
        data=request.json
        
        categoryTable(data)
        productTable(data)

        return {"Data Ingestion":"Successfull!!!"}

api.add_resource(upload,"/upload")


#fetches ten products from unbxd search api and return it
class productQuery(Resource):
    @cache.cached(timeout=30, query_string=True)
    def get(self):
        searchQuery = request.args.get('q', default="", type=str)
        pageNumber = request.args.get('page', default=1, type=int)
        sortKey = request.args.get('sort', default="ftrd", type=str)
        print(searchQuery,pageNumber,sortKey)
        pageNumber=(pageNumber-1)*9
        if sortKey=='ftrd':
            response = searchProduct(searchQuery,pageNumber,"")
        else:
            response=searchSorted(searchQuery,sortKey,pageNumber)
        #response=searchProduct(searchQuery,pageNumber,sortKey)
        data = json.loads(response.content)
        products = data['response']['products']
        productsNumber = data['response']['numberOfProducts']
        return [productsNumber,products]

api.add_resource(productQuery,"/product_query")


#fetch products from certain category
class category(Resource):
    @cache.cached(timeout=30, query_string=True)
    def get(self): #page number should also be an argument
        catLevel1 = request.args.get('cat1', default="", type=str)
        catLevel2 = request.args.get('cat2', default="", type=str)
        pageNumber = request.args.get('page', default=1, type=int)
        sortKey = request.args.get('sort', default="ftrd", type =str)
        pageNumber=(pageNumber-1)*9
        data=searchProducts(catLevel1,catLevel2)
        #print(data)
        new_data = []
        for product in data:
            new_data.append({"uniqueId":product[0], "Title":product[1], "Description":product[2],"Img_URL":product[3],"price":product[4]})
        
        if(sortKey=="price asc"):
            new_data = sorted(new_data, key=lambda k: float(k['price']))
        if(sortKey=="price desc"):
            new_data = sorted(new_data, key=lambda k: float(k['price']), reverse=True)
        
        
        sliced_data=new_data[pageNumber:pageNumber+9]   
        return [len(new_data),sliced_data]

api.add_resource(category,"/category")

class productSort(Resource):
    @cache.cached(timeout=30, query_string=True)
    def get(self,searchQuery,sortKey,pageNumber):
        pageNumber=max((pageNumber-1)*9,1)
        if sortKey=='ftrd':
            response = searchProduct(searchQuery,pageNumber,"")
        else:
            response=searchSorted(searchQuery,sortKey,pageNumber)
        data = json.loads(response.content)
        products = data['response']['products']
        productsNumber = data['response']['numberOfProducts']
        return [productsNumber,products]

api.add_resource(productSort,"/product_query/<string:searchQuery>/<string:sortKey>/<int:pageNumber>")

class categorySort(Resource):
    @cache.cached(timeout=30, query_string=True)
    def get(self): #page number should also be an argument
        catLevel1 = request.args.get('cat1', default="", type=str)
        catLevel2 = request.args.get('cat2', default="", type=str)
        sortKey = request.args.get('sort', default="ftrd", type =str)
        pageNumber = request.args.get('page', default=1, type=int)
        pageNumber=(pageNumber-1)*9
        print(sortKey)
        data=searchProducts(catLevel1,catLevel2)
        type(data)
        new_data=[]
        for product in data:
            new_data.append({"uniqueId":product[0], "Title":product[1].capitalize(), "Description":product[2],"Img_URL":product[3],"price":product[4]})
        
        if(sortKey=="price asc"):
            new_data = sorted(new_data, key=lambda k: float(k['price']))
        if(sortKey=="price desc"):
            new_data = sorted(new_data, key=lambda k: float(k['price']), reverse=True)

        sliced_data=new_data[pageNumber:pageNumber+9]

        return [len(new_data),sliced_data]

api.add_resource(categorySort,"/categorySort")


if __name__=='__main__':
    app.run(port=7002,debug=True,host = "0.0.0.0")


#future work


#update the product details if the product already exists in the database and the product_id is valid
# class updateProduct(Resource):
#     def put(self):
#         data=request.json
#         for i in data:
#             productId=i.get("uniqueId")
#             if(productId==None):
#                 print({"Message":"Product ID is not given"})
#                 break
#             if(checkProductID(productId)==0):
#                 print({"Message":"Product ID is missing in DB"})
#                 break
#             updateDB(i.get("title"),i.get("productDescription"),i.get("productImage"),i.get("price"),productId)
            
#         return({"Message":"DB Updated","status":200})

# api.add_resource(updateProduct,"/updateProduct")  