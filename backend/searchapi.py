import requests

def searchProduct(searchQuery,pageNumber):
    unbxdApi = f"https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?q={searchQuery}&rows=9&start={pageNumber}"
    response=requests.get(unbxdApi)
    return response

def searchSorted(searchQuery,SortKey):
    print(SortKey)
    unbxdApi = f"https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?q={searchQuery}&sort={SortKey}&rows=9&start=1"
    response=requests.get(unbxdApi)
    return response

#new comment