# Basic Summary
The prpoject consists of two components: Frontend and Backend.
Backend is coded using Pythion and Flask.
Frontend is using HTML and javascript.
All the API are restful and are made using flask_resftul module.

# API Spec

- Data Ingestion:
    POST   /upload   HTTP/1.1
    Host: localhost
    Content-Type: application/json
    {
    JSON
    }
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
    GET /product_query HTTP/1.1<br>
    Host: localhost<br>
    Arguments:  <br>
                'q', default="", type=str<br>
                'page', default=1, type=int<br>
                'sort', default="ftrd", type=str<br>
<br>
<br>
- Product Sort<br>
    GET /product_query/<string:searchQuery>/<string:sortKey>/<int:pageNumber> HTTP/1.1<br>
    Host: localhost<br>
<br>
<br>
- Category Sort<br>
    GET /categorySort HTTP/1.1<br>
    Host: localhost<br>
    Arguments:<br>
                'cat1', default="", type=str<br>
                'cat2', default="", type=str<br>
                'sort', default="ftrd", type =str<br>
                'page', default=1, type=int<br>

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
- Run: docker-compose up -d --build
- On terminal run this command for data ingestion into database :
        curl http://127.0.0.1:7002/upload -d @out.json -H "Content-Type: application/json

To run frontend:
- docker build -t zoro:v1 . 
- docker run -d -p 80:80 zoro:v1

Now, both the frontend and backend will be running in docker.
Open localhost for user interface







