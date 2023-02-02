function getQuery(){
  let searchQuery = document.getElementById("query").value
  console.log(searchQuery)
  window.parent.location=`index.html?q=${searchQuery}&page=1`;
}

function home(){
  window.parent.location=`index.html?q=*`;
}
  
function getCategory(cat1,cat2){
  window.parent.location=`index.html?cat1=${cat1}&cat2=${cat2}&page=1&sort=`;
}