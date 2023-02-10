import { generateCategory } from "./category.js";

window.onload = function () {
  generateCategory();
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  let uniqueId = urlParams.get('uid');
  let prod_query = urlParams.get('q');

  if (prod_query === "") {
    let prod_query = '*';
  }

  if (uniqueId != null) {
    fetch(`http://127.0.0.1:7002/product/${uniqueId}`, {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=utf-8',

      }
    }).then(response => {
      const statusCode = response.status;
      if ((statusCode < 300) && (statusCode >= 200)) {
        response.json().then(data => {
          try {
            if (data === null) throw "Unable to fetch data";
            let prod_container = document.getElementById("row");
            let decimal = (parseFloat(data['price']).toFixed(2)).slice(-2);
            let price = String(parseInt(data['price']));
            prod_container.innerHTML += `<div class="column1">
                <img class="image" src="${data['image_url']}">
            </div>
            <div class="column2">
                <p class="image_title">${data['title']}</p>
                <p class="price"><sup>$</sup>${price}<sup>${decimal}</sup></p>
                <p class="image_body">${data['description']}</p>
            </div>`
          }
          catch (err) {
            alert(err);
            window.parent.location = `404.html`;
          }
        });
      }
      else if ((statusCode < 500) && (statusCode >= 400)) {
        window.parent.location = `404.html`;
      }

      else if ((statusCode < 600) && (statusCode >= 500)) {
        window.parent.location = `404.html`;
      }

      else {
        ;
      }
    }).catch(err=>{
      let prod_container = document.getElementById("row");
          prod_container.innerHTML += `</div>
        <img src="images/error500.png" class="error">
        </div>`
    });
  }
  else {
    window.parent.location = `index.html?q=${prod_query}&page=1`
  }
}
