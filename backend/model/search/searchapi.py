import requests,json

def searchProduct(searchQuery,pageNumber,sortKey):
    '''
    Sends a get request to nbxd search api and returns the response.
    input agruments are search query,page number and sort key.
    '''
    if sortKey=='ftrd':
        sortKey=""
    unbxdApi = f"https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?q={searchQuery}&rows=9&start={pageNumber}&sort={sortKey}"
    response=requests.get(unbxdApi)
    data = json.loads(response.content)
    products = data['response']['products']
    productsNumber = data['response']['numberOfProducts']
    return [products,productsNumber]

'''def searchSorted(searchQuery,SortKey,pageNumber):
    print(SortKey)
    unbxdApi = f"https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?q={searchQuery}&sort={SortKey}&rows=9&start={pageNumber}"
    response=requests.get(unbxdApi)
    return response
    '''

