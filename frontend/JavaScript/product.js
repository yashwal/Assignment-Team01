window.onload = function(){
    fetch(`http://127.0.0.1:7002/categoryTree`,{
    method : 'GET',
    mode :'cors',
    headers:{
      'Access-Control-Allow-Origin':'*',
      'Accept': 'application/json',
      'Content-Type': 'application/json;charset=utf-8',
      
    }
    
  }).then(response => response.json()).then(data =>{
    cat1 = data[0];
    cat2 = data[1];
    cat3 = data[2];
    var cat_container=document.getElementById("dropdownheader");
    cat_container.innerHTML =``;
    for( let i = 0; i < cat1.length; i++){
      var catId = cat1[i][1];
      var catValue = cat1[i][0];
      var value = cat1[i][0];
      if (catValue!='exp'){
      dataElement = data[parseInt(catId)+1];
      var elementArr = dataElement[catId].sort();
      var tempo = ``;
      for( let j = 0;j < elementArr.length; j++){
        var valueName = elementArr[j].replace(/([A-Z])/g, ' $1').trim();
        tempo += `<li onclick="getCategory('${catId}','${elementArr[j]}')" class="hover-button">${valueName}</li>`;
      }
      }
      if (catValue=='exp'){
        value = 'Others';
        cat_container.innerHTML += `<div class="right-menu">
        <button class="button" onclick="getCategory('${catId}','${value}')">Gift Cards</button>
        </div>`;
      }
      else{
      cat_container.innerHTML += `<div class="right-menu">
      <button class="button" onclick="getCategory('${catId}',value)" value="${value}">${catValue}</button>
      <div class="dropdown-menu">` + tempo;
      }
    }
  });
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    var uniqueId =urlParams.get('uid');
    var prod_query =urlParams.get('q');

  if(prod_query==""){
    var prod_query='*';
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
      var prod_container=document.getElementById("row");
          prod_container.innerHTML+=`<div class="column1">
              <img class="image" src="${data['image_url']}">
          </div>
          <div class="column2">
              <p class="image_title">${data['title']}</p>
              <p class="price">$ ${data['price']}</p>
              <p class="image_body">${data['description']}</p>
          </div>`
  }).catch(err=>{
    console.log(err);
  });}
  else{
    window.parent.location=`index.html?q=${prod_query}&page=1`
  }
  }
  