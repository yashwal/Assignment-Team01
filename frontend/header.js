function getQuery(){
  let searchQuery = document.getElementById("query").value
  console.log(searchQuery)
  window.parent.location=`index.html?q=${searchQuery}`;
}

function home(){
  window.parent.location=`index.html?q=${'*'}`;
}
  
function getCategory(cat1){
  let selector;
  let cat2;
  if (cat1=='0'){
    selector = document.querySelector("#cat1")
    //cat1 = 'men'
    cat2 = selector.value;
  }
  else if (cat1=='1'){
     selector = document.querySelector("#cat2")
     //cat1 = 'women'
     cat2 = selector.value;
  }
  else{
    cat1 = '2'
    cat2 = "Others"
  }
  console.log(cat1);
  console.log(cat2);
  window.parent.location=`index.html?cat1=${cat1}&cat2=${cat2}`
}