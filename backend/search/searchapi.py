import requests

def searchProduct(searchQuery,pageNumber,sortKey):
    '''
    Sends a get request to nbxd search api and returns the response.
    input agruments are search query,page number and sort key.
    '''
    unbxdApi = f"https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?q={searchQuery}&rows=9&start={pageNumber}&sort={sortKey}"
    response=requests.get(unbxdApi)
    return response





