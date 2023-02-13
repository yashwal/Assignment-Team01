function fetchSortKey(){
    let selector = document.querySelector("#sort");
    sortKey = selector.value;
    return sortKey;
}

function home(){
    window.parent.location=`index.html?q=*`;
  }
    

function prevPage(){
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    let prod_query =urlParams.get('q');
    let sortKey = urlParams.get('sort');
    let catId = urlParams.get('catid');
    if ((sortKey===null)||(sortKey==='null'||sortKey==="")){
        sortKey = fetchSortKey();
    }
    let pageNumber = document.getElementById('pageNumber').value-1;
    pageNumber -= 1;
    if ((pageNumber >= 1)&&(sortKey!==null)&&(prod_query!==null)){
        window.parent.location = `index.html?q=${prod_query}&page=${pageNumber}&sort=${sortKey}`
    }
    if ((pageNumber >= 1)&&(sortKey!==null)&&(catId!==null)){
        window.parent.location = `index.html?catid=${catId}&page=${pageNumber}&sort=${sortKey}`
    }
}

function nextPage(){
    let queryString = window.location.search;
    let urlParams = new URLSearchParams(queryString);
    let prod_query = urlParams.get('q');
    let sortKey = urlParams.get('sort');
    let catId = urlParams.get('catid');
    if ((sortKey===null)||(sortKey==='null'||sortKey==="")){
        sortKey = fetchSortKey();
    }
    if (sortKey===""){
        sortKey = "ftrd";
    }
    
    let pageNumber = document.getElementById('pageNumber').value-1;
    pageNumber += 1;
    if ((pageNumber >= -1000)&&(sortKey!==null)&&(prod_query!==null)){
        window.parent.location = `index.html?q=${prod_query}&page=${pageNumber}&sort=${sortKey}`
    }
    if ((pageNumber >= 1)&&(sortKey!==null)&&(catId!==null)){
        window.parent.location = `index.html?catid=${catId}&page=${pageNumber}&sort=${sortKey}`
    }
}