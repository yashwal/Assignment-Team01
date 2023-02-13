function getQuery(){
  let searchQuery = document.getElementById("query").value
  window.parent.location=`index.html?q=${searchQuery}&page=1`;
}

function home(){
  window.parent.location=`index.html?q=*`;
}
  
function getCategory(catId){
  window.parent.location=`index.html?catid=${catId}&page=1&sort=`;
}

