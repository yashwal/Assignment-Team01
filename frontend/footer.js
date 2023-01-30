
function prevPage(){
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    prod_query =urlParams.get('q');
    var pageNumber = document.getElementById('pageNumber').value-1;
    pageNumber -= 1;
    if (pageNumber >= -10000){
        window.parent.location = `index.html?q=${prod_query}&page=${pageNumber}`
    }
}

function nextPage(){
    var queryString = window.location.search;
    console.log(queryString)
    var urlParams = new URLSearchParams(queryString);
    var prod_query =urlParams.get('q');
    var pageNumber = document.getElementById('pageNumber').value-1;
    pageNumber += 1;
    if (pageNumber >= -1000){
        window.parent.location = `index.html?q=${prod_query}&page=${pageNumber}`
    }
}