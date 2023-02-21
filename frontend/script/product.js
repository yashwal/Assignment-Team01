import { generateCategory } from "./category.js";

function star(value){
  let point = String((parseFloat(value).toFixed(2))).slice(-2);
  let disp = ``;
  let i;
  for(i=1;i<=value;i++){
    disp += `<i class="fa fa-star full-star" style="font-size:24px"></i>`;
  }
  if (point==='50')
    disp += `<i class="fa fa-star-half-o full-star" style="font-size:24px"></i>`;
  return disp;
}

let recommend_container = document.getElementById("similarProducts");
recommend_container.innerHTML = ``;

function fetchRecommended(productId) {
  fetch(`http://127.0.0.1:7002/product/${productId}`, {
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
            let decimal = (parseFloat(data['price']).toFixed(2)).slice(-2);
            let price = String(parseInt(data['price']));
            let rating = parseFloat(data['rating']);
            let disp = star(rating);
            recommend_container.innerHTML += `<div class="col" onclick="window.open('product.html?uid=${productId}','_self')">
                <img class="rec_image" src="${data['image_url']}">
                <p class="rec_image_text">${data['title']}</p>
                <p class="rating">${disp}</p>
                <p class="rec_price"><sup>$</sup>${price}<sup>${decimal}</sup></p>
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

window.onload = function () {
  generateCategory();
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  let uniqueId = urlParams.get('uid');
  let prod_query = urlParams.get('q');

  if (prod_query === "") {
       prod_query = '*';
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
            let rating = parseFloat(data['rating']);
            let disp = star(rating);
            prod_container.innerHTML += `<div class="column1">
                <img class="image" src="${data['image_url']}">
            </div>
            <div class="column2">
                <p class="image_title">${data['title']}</p>
                <p class="price"><sup id="sup_price">$</sup>${price}<sup id="sup_price">${decimal}</sup></p>
                <p class="rating">${disp}</p>
                <p class="image_body">${data['description']}</p>
            </div>`
          }
          catch (err) {
            alert(err);
            // window.parent.location = `404.html`;
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

    fetch(`http://127.0.0.1:7002/recommend/${uniqueId}`, {
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
            for(let i=0;i<data.length;i++){
              fetchRecommended(data[i]);
            }
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
