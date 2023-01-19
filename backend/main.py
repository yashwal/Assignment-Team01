from flask import *
from flask_restful import Api,Resource
from dataAccess import *

app=Flask(__name__)
api=Api(app)

class fetchProducts(Resource):
    def get(self,productId):
        data=getProducts(productId)
        return data
        
api.add_resource(fetchProducts,"/fetchProducts/<string:productId>")

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


class upload(Resource):
    def post(self):
        data=request.json
        uploadProduct(data)
        uploadCategory(data)
        return {"Data Ingestion":"Successfull!!!"}

api.add_resource(upload,"/upload")


if __name__=='__main__':
    app.run(port=7000,debug=True)


'''
else:
                if(i.get("title")!=None):
                    updateTitle(i.get("title"),productId)
                
                if(i.get("productDescription")!=None):
                    updateDesc(i.get("productDescription"),productId)

                if(i.get("productImage")!=None):
                    updateUrl(i.get("productImage"),productId)

                if(i.get("price")!=None):
                    updatePrice(i.get("price"),productId)
'''