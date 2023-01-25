from flask import *
import requests
import json
from flask_cors import CORS
from flask_restful import Api,Resource
from searchapi import *
from dataRetrieval import *
#from searchapi import *

app = Flask(__name__)
CORS(app)

@app.route('/product-query')

def productQuery():
    query_val = request.args.get('q', default="", type=str)
    response = requests.get(f'https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?q={query_val}')
    data = json.loads(response.content)
    product = data['response']['products']
    return data['response']['products']

    
@app.route('/category')

def categoryQuery():
    catLevel1 = request.args.get('cat1', default="", type=str)
    catLevel2 = request.args.get('cat2', default="", type=str)
    data=searchProducts(catLevel1,catLevel2)
    new_data = []
    for product in data:
        new_data.append({"uniqueId":product[0], "Title":product[1], "Description":product[2],"Img_URL":product[3],"price":product[4]})
    print(new_data,len(catLevel2))
    return new_data

if __name__ == "__main__":
    app.run(port=6969,debug=True)
