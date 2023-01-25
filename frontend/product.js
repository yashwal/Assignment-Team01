window.onload = function(){
    const queryString = window.location.search;
    
    const urlParams = new URLSearchParams(queryString);
    var uniqueId =urlParams.get('uid')
   
        fetch(`http://127.0.0.1:7000/product/${uniqueId}`,{
        method : 'GET',
        mode :'cors',
        headers:{
        'Access-Control-Allow-Origin':'*',
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=utf-8',
        
        }
  }).then(response => response.json()).then(data =>{
    console.log(uniqueId,"kkkk")
      var prod_container=document.getElementById("row");
          prod_container.innerHTML+=`<div class="column1">
              <img class="image" src="${data['image_url']}">
          </div>
          <div class="column2">
              <p class="image_path">Home/Product/${uniqueId}</p>
              <p class="image_title">${data['title']}</p>
              <p class="price">$ ${data['price']}</p>
              <p class="image_body">${data['description']}</p>
          </div>`
  }).catch(err=>{
    console.log(err);
  });
  }
  