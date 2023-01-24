from flask import *
from flask_restful import Api,Resource


from dataRetrieval import *
from dataInsertion import *
from dataUpdation import *
from searchapi import *
import json


app=Flask(__name__)
api=Api(app)


#product_id is given as input , returns the product details
class fetchProducts(Resource):
    def get(self,productId):
        data=getProducts(productId)
        return data
api.add_resource(fetchProducts,"/fetchProducts/<string:productId>")



#update the product details if the product already exists in the database and the product_id is valid
class updateProduct(Resource):
    def put(self):
        data=request.json
        for i in data:
            productId=i.get("uniqueId")
            if(productId==None):
                print({"Message":"Product ID is not given"})
                break
            if(checkProductID(productId)==0):
                print({"Message":"Product ID is missing in DB"})
                break
            updateDB(i.get("title"),i.get("productDescription"),i.get("productImage"),i.get("price"),productId)
            
        return({"Message":"DB Updated","status":200})

api.add_resource(updateProduct,"/updateProduct")               


#upload the given data in the json file to postgreSQL table
class upload(Resource):
    def post(self):
        data=request.json
        uploadProduct(data)
        uploadCategory(data)

        return {"Data Ingestion":"Successfull!!!"}

api.add_resource(upload,"/upload")


#fetches ten products from unbxd search api and return it
class productQuery(Resource):
    def get(self,searchQuery):
        #searchQuery = request.args.get('q', default="", type=str)

        response=searchProducts(searchQuery)
        data = json.loads(response.content)
        products = data['response']['products']
        return products

api.add_resource(productQuery,"/product_query/<string:searchQuery>")


#fetch products from certain category
class category(Resource):
    def get(self,catLevel1,catLevel2): #page number should also be an argument
        data=getCategory(catLevel1,catLevel2)
        new_data = []
        for product in data:
            new_data.append({"uniqueId":product[0], "Title":product[1], "Description":product[2],"Img_URL":product[3],"price":product[4]})

        return new_data
api.add_resource(category,"/category/<string:catLevel1>&<string:catLevel2>")

if __name__=='__main__':
    app.run(port=7000,debug=True)


