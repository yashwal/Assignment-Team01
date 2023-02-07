import sys
sys.path.append('..')
from flask import request
from flask_restful import Resource
from model.category.categoryInsertion import *
from model.category.categoryRetreival import *
from model.product.productInsertion import *
from model.product.productRetreival import *
from model.search.searchapi import *
from app import api,cache,host

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
        
        [length,sliced_data]=searchProducts(catLevel1,catLevel2,sortKey,pageNumber)

        return [length,sliced_data]
api.add_resource(category,"/category")

if __name__=='__main__':
    host()
