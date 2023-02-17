import sys
sys.path.append('..')
from flask import request
from flask_restful import Resource
from category.controller.categoryInsertion import *
from category.controller.categoryRetreival import *
from products.controller.productInsertion import *
from products.controller.productRetreival import *
from recommendations.controller.recommend import *
from search.searchapi import *
from app import api,cache,host


class upload(Resource):
    '''
    upload the given data in the json file to postgreSQL table
    '''
    def post(self):
        data=request.json
        categoryTable(data)
        res=productTable(data)
        pkldump()
        return res
api.add_resource(upload,"/upload")


class fetchProducts(Resource):
    '''
    product_id is given as input , returns the product details
    '''
    @cache.cached(timeout=30, query_string=True)
    def get(self,productId):
        return getProducts(productId)
api.add_resource(fetchProducts,"/product/<string:productId>")

class productQuery(Resource):
    '''
    fetches ten products from unbxd search api and return it
    '''
    @cache.cached(timeout=30, query_string=True)
    def get(self,searchQuery):
        print("entered controller")
        return searchProduct(searchQuery)      

api.add_resource(productQuery,"/product_query/<string:searchQuery>")

class categoryTree(Resource):
    ''''
    creates category tree for category level 1 and level 2. Returns a JSON file with category heirarchy
    '''
    @cache.cached(timeout=30, query_string=True)
    def get(self):
        return categoryLevel()
api.add_resource(categoryTree,"/categoryTree")


class category(Resource):
    '''
    fetch products for the given category
    '''
    @cache.cached(timeout=30, query_string=True)
    def get(self,catId): 
        return searchCategory(catId)
api.add_resource(category,"/category/<string:catId>")

class recommend(Resource):
    '''
    product_id is given as input , returns the product details
    '''
    @cache.cached(timeout=30, query_string=True)
    def get(self,productId):
        return getRecommendation(productId)
api.add_resource(recommend,"/recommend/<string:productId>")

if __name__=='__main__':
    host()
