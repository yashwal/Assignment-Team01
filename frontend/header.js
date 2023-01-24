function getQuery(){
    let searchQuery = document.getElementById("query").value
    console.log(searchQuery)
    window.parent.location=`index.html?q=${searchQuery}`;
  }
    
  function getCategory(cat1){
    let selector;
    let cat2;
    if (cat1=='0'){
      selector = document.querySelector("#cat1")
      cat2 = selector.value;
    }
    else if (cat1=='1'){
       selector = document.querySelector("#cat2")
       cat2 = selector.value;
    }
    else{
      cat2 = "Others"
    }
    console.log(cat1);
    console.log(cat2);
    window.parent.location=`index.html/category/${cat1}/${cat2}`
  }