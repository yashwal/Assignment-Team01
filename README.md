# Klothing.com
The prpoject consists of two components: Frontend and Backend.
Backend is coded using Pythion and Flask.
Frontend is using HTML and javascript.
All the API are restful and are made using flask_resftul module.

<br>
<br>
# PPT Link
https://www.canva.com/design/DAFaeD5Wo-8/MzYFwVJ9_aiEYEOXln6vjw/view?utm_content=DAFaeD5Wo-8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

<br>
<br>
# API Spec

- Data Ingestion:
     POST 
    "/upload"  HTTP/1.1
    Host: localhost
    Content-Type: application/json
- input should be out.json file
<br>
<br>
- Fetch Product:<br>
    GET /product/<string:productId> HTTP/1.1<br>
    Host: localhost<br>
<br>
<br>
- Category Tree<br>
    GET /categoryTree HTTP/1.1<br>
    Host: localhost<br>
<br>
<br>
- Product Query<br>
     GET 
    "/product_query/<string:searchQuery>"  HTTP/1.1
    Host: klothing.com 
<br>
<br>
- Category <br>
    GET 
    "/category/<string:catId>"  HTTP/1.1
    Host: klothing.com 
<br>
<br>
<br>


# add this file to unbxd training/Assignment-Team01 folder
.env<br>
CACHE_TYPE=redis<br>
CACHE_REDIS_HOST=redis<br>
CACHE_REDIS_PORT=6379<br>
CACHE_REDIS_DB=0<br>
CACHE_REDIS_URL=redis://redis:6379/0<br>
CACHE_DEFAULT_TIMEOUT=500<br>
<br>

# Docker Installation Instruction
To run backend:
- Go to Assignment folder
- Run:  minikube start

        minikube tunnel

        In build folder run:
        kubectl apply -f adminer-deployment.yaml,adminer-service.yaml,api-deployment.yaml,api-service.yaml,assignment-team01-default-networkpolicy.yaml,database-deployment.yaml,database-service.yaml,env-configmap.yaml,redis-deployment.yaml,redis-service.yaml,frontend-deployment.yaml,frontend-tcp-service.yaml

         kubectl port-forward deployment/api 7002:7002

- On terminal run this command for data ingestion into database :
        curl http://127.0.0.1:7002/upload -d @out.json -H "Content-Type: application/json

In browser:
- Open localhost to access GUI
<br>
<br>


Screenshots:
<br>
## Homepage<br>
![Homepage](/Screenshots/Homepage.png)
<br>
## Product display page
![product page ](Screenshots/Product_Display_Page.png)
<br>
## Recommendations  
![Recommendations ](Screenshots/recommended_products.png)
<br>
## Filter
![Filter](Screenshots/Filter.png)
<br>
## Pagination
![Pagination](Screenshots/Pagination.png)
<br>
## Search Page
![Search Page](Screenshots/Products_after_query.png)
<br>
## Category Dropdown 
![Category](Screenshots/Category_Dropdown.png)
<br>
## Filter Dropdown 
![filter ](Screenshots/Filter_Dropdown.png)
<br>













