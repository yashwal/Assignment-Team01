function sortedView(){
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  let prod_query=null;
  let catLevel1=null;
  let catLevel2=null;
  let pageNumber = 1;
  prod_query = urlParams.get('q');
  catLevel1 = urlParams.get('cat1');
  catLevel2 = urlParams.get('cat2');
  //pageNumber = urlParams.get('page');
  urlSortKey = urlParams.get('sort')

  selector = document.querySelector("#sort");
  sortKey = selector.value;
  console.log(sortKey)

  if (prod_query!=null){
    window.parent.location = `index.html?q=${prod_query}&page=1&sort=${sortKey}`
    fetch(`http://127.0.0.1:7002/product_query/${prod_query}/${sortKey}/1`,{
      method : 'GET',
      mode :'cors',
      headers:{
        'Access-Control-Allow-Origin':'*',
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=utf-8',
        
      }
      
    }).then(response => response.json()).then(data =>{
        var pages = data[0]
        var pageTotal = Math.ceil(pages/9);
        var data = data[1];
        console.log((pageNumber-1)*9,(pageNumber-2)*9)
        var prod_container=document.getElementById("outer-div");
        prod_container.innerHTML = '';
        if(data.length==0){
          prod_container.innerHTML+= `</div>
          <img src="iamge.jpg" width="1100" height="700" class="center">
          </a>
          </div>`
        }
        for( let i = 0; i < data.length; i++){
            prod_container.innerHTML+=`<div class="column" id="uid" onclick="window.open('product.html?uid=${data[i]['uniqueId']}','_self')">
            <img class="image" src="${data[i]['imageUrl'][0]}">
            <p class="image_text" >${data[i]['title']}</p>
            <p class="price">$ ${data[i]['price']}</p>
            </a>
        </div>`
        }
        pageNumber++;
        var pageDisplay = ""
        var footer_container = document.getElementById("footer-div");
        if ((pageNumber-1)*9 < pages){
          pageDisplay = `Showing ${(pageNumber-2)*9+1}-${(pageNumber-1)*9} of ${pages} products`;
          footer_container.innerHTML = ` <ul class="page">
        <li class="text-footer" onclick="prevPage()"> &lt; </li>
        <li class="text-footer" id="pageNumber" value="${pageNumber}"> ${pageNumber-1} </li>
        <li class="text-footer" onclick="nextPage()"> &gt; </li>
        <li class="product-text">${pageDisplay}</li></ul>`
        }
        else if (((pageNumber-2)*9+1 <= pages)&&((pageNumber-1)*9+1 > pages)){
          pageDisplay = `Showing ${(pageNumber-2)*9+1}-${pages} of ${pages} products`;
          footer_container.innerHTML = ` <ul class="page">
        <li class="text-footer" onclick="prevPage()"> &lt; </li>
        <li class="text-footer" id="pageNumber" value="${pageNumber}"> ${pageNumber-1} </li>
        <li class="text-footer" onclick="nextPage()"> &gt; </li>
        <li class="product-text">${pageDisplay}</li></ul>`
        }
        else{
          pageDisplay = ``;
          footer_container.innerHTML = ` <ul class="page">
        <li class="return-home" onclick="home()">Return to Home</li>
        <li></li>
        <li></li>
        <li></li></ul>`
        }
    });
  }

  else if (catLevel1!=null ){
    window.parent.location = `index.html?cat1=${catLevel1}&cat2=${catLevel2}&page=${pageNumber}&sort=${sortKey}`
    console.log(sortKey)
    fetch(`http://127.0.0.1:7002/categorySort?cat1=${catLevel1}&cat2=${catLevel2}&page=${pageNumber}&sortKey=${sortKey}`,{
      method : 'GET',
      mode :'cors',
      headers:{
        'Access-Control-Allow-Origin':'*',
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=utf-8',
        
      }
      
    }).then(response => response.json()).then(data =>{
        var pageTotal = Math.ceil(data[0]/9);
        console.log(pageTotal)
        var data = data[1];
        var prod_container=document.getElementById("outer-div");
        prod_container.innerHTML = '';
        for( let i = 0; i < data.length; i++){
            prod_container.innerHTML+=`<div class="column" name="uid" onclick="window.open('product.html?uid=${data[i]['uniqueId']}','_self')">
            <img class="image" src="${data[i]['Img_URL']}">
            <p class="image_text">${data[i]['Title']}</p>
            <p class="price">$ ${data[i]['price']}</p>
            </a>
        </div>`
        }
        pageNumber++;
      var pageDisplay = ""
      var footer_container = document.getElementById("footer-div");
      if ((pageNumber-1)*9 < pages){
        pageDisplay = `Showing ${(pageNumber-2)*9+1}-${(pageNumber-1)*9} of ${pages} products`;
        footer_container.innerHTML = ` <ul class="page">
      <li class="text-footer" onclick="prevPage()"> &lt; </li>
      <li class="text-footer" id="pageNumber" value="${pageNumber}"> ${pageNumber-1} </li>
      <li class="text-footer" onclick="nextPage()"> &gt; </li>
      <li class="product-text">${pageDisplay}</li></ul>`
      }
      else if (((pageNumber-2)*9+1 <= pages)&&((pageNumber-1)*9+1 > pages)){
        pageDisplay = `Showing ${(pageNumber-2)*9+1}-${pages} of ${pages} products`;
        footer_container.innerHTML = ` <ul class="page">
      <li class="text-footer" onclick="prevPage()"> &lt; </li>
      <li class="text-footer" id="pageNumber" value="${pageNumber}"> ${pageNumber-1} </li>
      <li class="text-footer" onclick="nextPage()"> &gt; </li>
      <li class="product-text">${pageDisplay}</li></ul>`
      }
      else{
        pageDisplay = ``;
        footer_container.innerHTML = ` <ul class="page">
      <li class="return-home" onclick="home()">Return to Home</li>
      <li></li>
      <li></li>
      <li></li></ul>`
      }
    });
  }

    else {
      fetch(`http://127.0.0.1:7002/product_query/*/${sortKey}`,{
      method : 'GET',
      mode :'cors',
      headers:{
        'Access-Control-Allow-Origin':'*',
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=utf-8',
        
      }
      
    }).then(response => response.json()).then(data =>{
        var pageTotal = Math.ceil(data[0]/9);
        console.log(pageTotal)
        var data = data[1];
        var prod_container=document.getElementById("outer-div");
        prod_container.innerHTML = '';
        for( let i = 0; i < data.length; i++){
            prod_container.innerHTML+=`<div class="column" id="uid"  onclick="window.open('product.html?uid=${data[i]['uniqueId']}','_self')">
            <img class="image" src="${data[i]['imageUrl'][0]}">
            <p class="image_text">${data[i]['title']}</p>
            <p class="price">$ ${data[i]['price']}</p>
            </a>
        </div>`
        }
    });
  }
}

window.onload=function reload(){
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  var prod_query =urlParams.get('q');
  var catLevel1 =urlParams.get('cat1');
  var catLevel2 =urlParams.get('cat2');
  var pageNumber = urlParams.get('page')
  var sortKey = urlParams.get('sort')
  
  if (pageNumber==null){
    pageNumber = 1;
  }

  if (sortKey==null){
    sortKey = '';
  }

  if (prod_query!=null){
    fetch(`http://127.0.0.1:7002/product_query?q=${prod_query}&page=${pageNumber}&sort=${sortKey}`,{
    method : 'GET',
    mode :'cors',
    headers:{
      'Access-Control-Allow-Origin':'*',
      'Accept': 'application/json',
      'Content-Type': 'application/json;charset=utf-8',
      
    }
    
  }).then(response => response.json()).then(data =>{
      var pages = data[0]
      var pageTotal = Math.ceil(pages/9);
      console.log(data[0])
      var data = data[1];
      var prod_container=document.getElementById("outer-div");
      prod_container.innerHTML = '';
      if(data.length==0){
        prod_container.innerHTML+= `</div>
        <img src="iamge.jpg" width="1100" height="700" class="center">
        </a>
        </div>`
      }
      for( let i = 0; i < data.length; i++){
          prod_container.innerHTML+=`<div class="column" id="uid" onclick="window.open('product.html?uid=${data[i]['uniqueId']}','_self')">
          <img class="image" src="${data[i]['imageUrl'][0]}">
          <p class="image_text" >${data[i]['title']}</p>
          <p class="price">$${data[i]['price']}</p>
          </a>
      </div>`
      }
      pageNumber++;
      var pageDisplay = ""
      var footer_container = document.getElementById("footer-div");
      if ((pageNumber-1)*9 < pages){
        pageDisplay = `Showing ${(pageNumber-2)*9+1}-${(pageNumber-1)*9} of ${pages} products`;
        footer_container.innerHTML = ` <ul class="page">
      <li class="text-footer" onclick="prevPage()"> &lt; </li>
      <li class="text-footer" id="pageNumber" value="${pageNumber}"> ${pageNumber-1} </li>
      <li class="text-footer" onclick="nextPage()"> &gt; </li>
      <li class="product-text">${pageDisplay}</li></ul>`
      }
      else if (((pageNumber-2)*9+1 <= pages)&&((pageNumber-1)*9+1 > pages)){
        pageDisplay = `Showing ${(pageNumber-2)*9+1}-${pages} of ${pages} products`;
        footer_container.innerHTML = ` <ul class="page">
      <li class="text-footer" onclick="prevPage()"> &lt; </li>
      <li class="text-footer" id="pageNumber" value="${pageNumber}"> ${pageNumber-1} </li>
      <li class="text-footer" onclick="nextPage()"> &gt; </li>
      <li class="product-text">${pageDisplay}</li></ul>`
      }
      else{
        pageDisplay = ``;
        prod_container.innerHTML+= `</div>
        <img src="iamge.jpg" width="1000" height="650" class="center">
        </a>
        </div>`;
        footer_container.innerHTML = ` <ul>
      <li class="return-home" onclick="home()">Return to Home</li></ul>`
      }
  });
  }
    else if (catLevel1!=null ){
      fetch(`http://127.0.0.1:7002/category?cat1=${catLevel1}&cat2=${catLevel2}&page=${pageNumber}&sort=${sortKey}`,{
      method : 'GET',
      mode :'cors',
      headers:{
        'Access-Control-Allow-Origin':'*',
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=utf-8',
        
      }
      
    }).then(response => response.json()).then(data =>{
      var pages = data[0]
        var pageTotal = Math.ceil(pages/9);
        // console.log(data[0])
        var data = data[1];
        var prod_container=document.getElementById("outer-div");
        prod_container.innerHTML = '';
        for( let i = 0; i < data.length; i++){
            prod_container.innerHTML+=`<div class="column" name="uid" onclick="window.open('product.html?uid=${data[i]['uniqueId']}','_self')">
            <img class="image" src="${data[i]['Img_URL']}">
            <p class="image_text">${data[i]['Title']}</p>
            <p class="price">$ ${data[i]['price']}</p>
            </a>
        </div>`
        }
        pageNumber++;
        var pageDisplay = ""
        var footer_container = document.getElementById("footer-div");
        if ((pageNumber-1)*9 < pages){
          pageDisplay = `Showing ${(pageNumber-2)*9+1}-${(pageNumber-1)*9} of ${pages} products`;
          footer_container.innerHTML = ` <ul class="page">
        <li class="text-footer" onclick="prevPage()"> &lt; </li>
        <li class="text-footer" id="pageNumber" value="${pageNumber}"> ${pageNumber-1} </li>
        <li class="text-footer" onclick="nextPage()"> &gt; </li>
        <li class="product-text">${pageDisplay}</li></ul>`
        }
        else if (((pageNumber-2)*9+1 <= pages)&&((pageNumber-1)*9+1 > pages)){
          pageDisplay = `Showing ${(pageNumber-2)*9+1}-${pages} of ${pages} products`;
          footer_container.innerHTML = ` <ul class="page">
        <li class="text-footer" onclick="prevPage()"> &lt; </li>
        <li class="text-footer" id="pageNumber" value="${pageNumber}"> ${pageNumber-1} </li>
        <li class="text-footer" onclick="nextPage()"> &gt; </li>
        <li class="product-text">${pageDisplay}</li></ul>`
        }
        else{
          pageDisplay = ``;
          prod_container.innerHTML+= `</div>
        <img src="iamge.jpg" width="1000" height="650" class="center">
        </a>
        </div>`;
          footer_container.innerHTML = ` <ul>
        <li class="return-home" onclick="home()">Return to Home</li></ul>`
        }
    });
  }
    else {
      fetch(`http://127.0.0.1:7002/product_query?q=*&page=${pageNumber}&sort=${sortKey}`,{
    method : 'GET',
    mode :'cors',
    headers:{
      'Access-Control-Allow-Origin':'*',
      'Accept': 'application/json',
      'Content-Type': 'application/json;charset=utf-8',
      
    }
    
  }).then(response => response.json()).then(data =>{
      var pageTotal = Math.ceil(data[0]/9);
      console.log(pageTotal)
      var data = data[1];
      var prod_container=document.getElementById("outer-div");
      prod_container.innerHTML = '';
      for( let i = 0; i < data.length; i++){
          prod_container.innerHTML+=`<div class="column" id="uid"  onclick="window.open('product.html?uid=${data[i]['uniqueId']}','_self')">
          <img class="image" src="${data[i]['imageUrl'][0]}">
          <p class="image_text">${data[i]['title']}</p>
          <p class="price">$ ${data[i]['price']}</p>
          </a>
      </div>`
      }
      pageNumber++;
      var pageDisplay = ""
      var footer_container = document.getElementById("footer-div");
      if ((pageNumber-1)*9 < pages){
        pageDisplay = `Showing ${(pageNumber-2)*9+1}-${(pageNumber-1)*9} of ${pages} products`;
        footer_container.innerHTML = ` <ul class="page">
      <li class="text-footer" onclick="prevPage()"> &lt; </li>
      <li class="text-footer" id="pageNumber" value="${pageNumber}"> ${pageNumber-1} </li>
      <li class="text-footer" onclick="nextPage()"> &gt; </li>
      <li class="product-text">${pageDisplay}</li></ul>`
      }
      else if (((pageNumber-2)*9+1 <= pages)&&((pageNumber-1)*9+1 > pages)){
        pageDisplay = `Showing ${(pageNumber-2)*9+1}-${pages} of ${pages} products`;
        footer_container.innerHTML = ` <ul class="page">
      <li class="text-footer" onclick="prevPage()"> &lt; </li>
      <li class="text-footer" id="pageNumber" value="${pageNumber}"> ${pageNumber-1} </li>
      <li class="text-footer" onclick="nextPage()"> &gt; </li>
      <li class="product-text">${pageDisplay}</li></ul>`
      }
      else{
        pageDisplay = ``;
        prod_container.innerHTML+= `</div>
        <img src="iamge.jpg" width="1000" height="650" class="center">
        </a>
        </div>`
        footer_container.innerHTML = ` <ul>
      <li class="return_home" onclick="home()">Return to Home</li>
      </ul>`
      }
  });
  }
}

