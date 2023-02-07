import { generateCategory } from "./category.js";

window.onload = function(){
    generateCategory();
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    let uniqueId =urlParams.get('uid');
    let prod_query =urlParams.get('q');

  if(prod_query===""){
    let prod_query='*';
  }

    if(uniqueId!=null){
        fetch(`http://127.0.0.1:7002/product/${uniqueId}`,{
        method : 'GET',
        mode :'cors',
        headers:{
        'Access-Control-Allow-Origin':'*',
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=utf-8',
        
        }
  }).then(response => response.json()).then(data =>{
      try{
        if (data===null) throw "Unable to fetch data";
        let prod_container=document.getElementById("row");
            prod_container.innerHTML+=`<div class="column1">
                <img class="image" src="${data['image_url']}">
            </div>
            <div class="column2">
                <p class="image_title">${data['title']}</p>
                <p class="price">$ ${data['price']}</p>
                <p class="image_body">${data['description']}</p>
            </div>`
      }
      catch(err){
        alert(err);
      }
  });}
  else{
    window.parent.location=`index.html?q=${prod_query}&page=1`
  }
  }
  