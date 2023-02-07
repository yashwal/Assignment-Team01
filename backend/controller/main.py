import sys
sys.path.append('..')

from flask import *
from flask_restful import Api,Resource
from flask_cors import CORS
from flask_caching import Cache

from model.category.categoryInsertion import *
from model.category.categoryRetreival import *
from model.product.productInsertion import *
from model.product.productRetreival import *
from model.search.searchapi import *
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


class categoryTree(Resource):
    @cache.cached(timeout=30, query_string=True)
    def get(self):
        data=categoryLevel()
        return data
api.add_resource(categoryTree,"/categoryTree")



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
        pageNumber=(pageNumber-1)*9
        [productsNumber,products] = searchProduct(searchQuery,pageNumber,sortKey)
        return [products,productsNumber]
        
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






if __name__=='__main__':
    app.run(port=7002,debug=True,host = "0.0.0.0")



# class productSort(Resource):
#     @cache.cached(timeout=30, query_string=True)
#     def get(self,searchQuery,sortKey,pageNumber):
#         pageNumber=max((pageNumber-1)*9,1)
#         if sortKey=='ftrd':
#             response = searchProduct(searchQuery,pageNumber,"")
#         else:
#             response=searchSorted(searchQuery,sortKey,pageNumber)
#         data = json.loads(response.content)
#         products = data['response']['products']
#         productsNumber = data['response']['numberOfProducts']
#         return [productsNumber,products]

# api.add_resource(productSort,"/product_query/<string:searchQuery>/<string:sortKey>/<int:pageNumber>")

# class categorySort(Resource):
#     @cache.cached(timeout=30, query_string=True)
#     def get(self): #page number should also be an argument
#         catLevel1 = request.args.get('cat1', default="", type=str)
#         catLevel2 = request.args.get('cat2', default="", type=str)
#         sortKey = request.args.get('sort', default="ftrd", type =str)
#         pageNumber = request.args.get('page', default=1, type=int)
#         pageNumber=(pageNumber-1)*9
#         print(sortKey)
#         data=searchProducts(catLevel1,catLevel2)
#         type(data)
#         new_data=[]
#         for product in data:
#             new_data.append({"uniqueId":product[0], "Title":product[1].capitalize(), "Description":product[2],"Img_URL":product[3],"price":product[4]})
        
#         if(sortKey=="price asc"):
#             new_data = sorted(new_data, key=lambda k: float(k['price']))
#         if(sortKey=="price desc"):
#             new_data = sorted(new_data, key=lambda k: float(k['price']), reverse=True)

#         sliced_data=new_data[pageNumber:pageNumber+9]

#         return [len(new_data),sliced_data]

#     api.add_resource(categorySort,"/categorySort")

