function getQuery(){
    let searchQuery = document.getElementById("query").value
    console.log(searchQuery)
    window.parent.location=`index.html?q=${searchQuery}`;
  }
    
  function getCategory1(){
    let selector = document.querySelector("#cat1");
    let cat1 = selector.name;
    let cat2 = selector.value;
    console.log(cat1);
    console.log(cat2);
  }

  function getCategory2(){
    let selector = document.querySelector("#cat2");
    let cat1 = selector.name;
    let cat2 = selector.value;
    console.log(cat1);
    console.log(cat2);
  }
