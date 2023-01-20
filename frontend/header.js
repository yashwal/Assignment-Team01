function getQuery(){
    let searchQuery = document.getElementById("query").value
    console.log(searchQuery)
    window.parent.location=`index.html?q=${searchQuery}`;
    fetch(`http://127.0.0.1:6969/product-query?q=${searchQuery}`,{
      method : 'GET',
      mode :'cors',
      headers:{
        'Access-Control-Allow-Origin':'*',
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=utf-8',
        
      }
    }).then(response => response.json()).then(data => console.log(data)).then(console.log("Done"));
  }
    
