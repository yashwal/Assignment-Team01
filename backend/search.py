from flask import *
import requests
import json
from flask_cors import CORS
from flask_restful import Api,Resource
from searchapi import *

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

    
if __name__ == "__main__":
    app.run(port=6969,debug=True)
