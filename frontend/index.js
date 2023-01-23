window.onload=function(){
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const prod_query =urlParams.get('q');

    if (prod_query!=null){
        fetch(`http://127.0.0.1:7000/product-query?q=${prod_query}`,{
      method : 'GET',
      mode :'cors',
      headers:{
        'Access-Control-Allow-Origin':'*',
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=utf-8',
        
      }
    }).then(response => response.json()).then(data =>{
        var prod_container=document.getElementById("outer-div");
        for( let i = 0; i < 9; i++){
            prod_container.innerHTML+=`<div class="column">
            <img class="image" src="${data[i]['imageUrl'][0]}">
            <p class="image_text">${data[i]['title']}</p>
            <p class="image_text">$${data[i]['price']}</p>
            </a>
        </div>`
        }
    });
    }
}