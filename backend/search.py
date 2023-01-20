from flask import *
from datetime import datetime
import requests
import json
from flask_cors import CORS
from searchapi import *

app = Flask(__name__)
CORS(app)

@app.route('/product-query')

def getQuery():
    searchQuery = request.args.get('q', default="", type=str)
    print(searchQuery)
    unbxdApi = f"https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?q={searchQuery}"
    response=requests.get(unbxdApi)
    data = json.loads(response.content)
    products = data['response']['products']
    product_title = {}
    for i in range(len(products)):
        product_title[i] = products[i]['title']
        print(product_title[i])
    return product_title
    
if __name__ == "__main__":
    app.run(debug=True,port=6969)