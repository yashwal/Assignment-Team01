window.onload=function(){
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const prod_query =urlParams.get('q');

    if (prod_query!=null){
        fetch(`http://127.0.0.1:6969/product-query?q=${prod_query}`, {
            method: 'GET',
            mode : 'cors',
            headers: {
            'Access-Control-Allow-Origin':'*',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            }}).then(response => response.json()).then(response=>console.log(response))
    }
}