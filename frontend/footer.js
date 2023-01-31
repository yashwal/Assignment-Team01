function fetchSortKey(){
    selector = document.querySelector("#sort");
    sortKey = selector.value;
    return sortKey;
}

function home(){
    window.parent.location=`index.html?q=*`;
  }
    

function prevPage(){
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    prod_query =urlParams.get('q');
    var sortKey = urlParams.get('sort');
    catLevel1 = urlParams.get('cat1');
    catLevel2 = urlParams.get('cat2');
    if ((sortKey==null)||(sortKey=='null'||sortKey=="")){
        sortKey = fetchSortKey();
    }
    var pageNumber = document.getElementById('pageNumber').value-1;
    pageNumber -= 1;
    if ((pageNumber >= 1)&&(sortKey!=null)&&(prod_query!=null)){
        window.parent.location = `index.html?q=${prod_query}&page=${pageNumber}&sort=${sortKey}`
    }
    if ((pageNumber >= 1)&&(sortKey!=null)&&(catLevel1!=null)){
        window.parent.location = `index.html?cat1=${catLevel1}&cat2=${catLevel2}&page=${pageNumber}&sort=${sortKey}`
    }
}

function nextPage(){
    var queryString = window.location.search;
    var urlParams = new URLSearchParams(queryString);
    var prod_query = urlParams.get('q');
    var sortKey = urlParams.get('sort');
    catLevel1 = urlParams.get('cat1');
    catLevel2 = urlParams.get('cat2');
    console.log(sortKey);
    if ((sortKey==null)||(sortKey=='null'||sortKey=="")){
        sortKey = fetchSortKey();
    }
    var pageNumber = document.getElementById('pageNumber').value-1;
    pageNumber += 1;
    if ((pageNumber >= -1000)&&(sortKey!=null)&&(prod_query!=null)){
        window.parent.location = `index.html?q=${prod_query}&page=${pageNumber}&sort=${sortKey}`
    }
    if ((pageNumber >= 1)&&(sortKey!=null)&&(catLevel1!=null)){
        window.parent.location = `index.html?cat1=${catLevel1}&cat2=${catLevel2}&page=${pageNumber}&sort=${sortKey}`
    }
}