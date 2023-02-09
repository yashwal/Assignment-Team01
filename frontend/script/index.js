import { generateCategory } from "./category.js";

function sortedView(sortKey) {
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  let prod_query = null;
  let catLevel1 = null;
  let catLevel2 = null;
  let pageNumber = 1;
  prod_query = urlParams.get('q');
  catLevel1 = urlParams.get('cat1');
  catLevel2 = urlParams.get('cat2');

  if (prod_query != null) {
    window.parent.location = `index.html?q=${prod_query}&page=1&sort=${sortKey}`
  }

  else if (catLevel1 != null) {
    window.parent.location = `index.html?cat1=${catLevel1}&cat2=${catLevel2}&page=${pageNumber}&sort=${sortKey}`
  }

  else {
    window.parent.location = `index.html?q=*&page=1&sort=${sortKey}`
  }
}

window.onload = function () {
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);

  let prod_query = urlParams.get('q');
  if (prod_query === "") {
    prod_query = '*';
  }
  let catLevel1 = urlParams.get('cat1');
  let catLevel2 = urlParams.get('cat2');
  let pageNumber = urlParams.get('page')
  let sortKey = urlParams.get('sort')

  if (pageNumber === null) {
    pageNumber = 1;
  }

  if (sortKey === null) {
    sortKey = '';
  }

  generateCategory();

  if (prod_query != null) {
    document.getElementById('loading').style.display = 'block';
    setTimeout(() => {
      fetch(`http://127.0.0.1:7002/product_query?q=${prod_query}&page=${pageNumber}&sort=${sortKey}`, {
        method: 'GET',
        mode: 'cors',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Accept': 'application/json',
          'Content-Type': 'application/json;charset=utf-8',

        }

      }).then(response => {
        console.log(response.status);
        const statusCode = response.status;
        if ((statusCode < 300) && (statusCode >= 200)) {
          response.json().then(data => {
            try {
              if (data === null) throw "Unable to fetch data";
              let pages = data[0]
              let pageTotal = Math.ceil(pages / 9);
              data = data[1];
              let prod_container = document.getElementById("outer-div");
              prod_container.innerHTML = '';

              let currentPage_container = document.getElementById("current_page");
              if (prod_query!=='*'){
              currentPage_container.innerHTML = `Showing Products for : "${prod_query}"`;
              }
              else{
                currentPage_container.innerHTML = `Showing All The Products`;
              }
              for (let i = 0; i < data.length; i++) {
                let decimal = (parseFloat(data[i]['price']).toFixed(2)).slice(-2);
                let price = String(parseInt(data[i]['price']));
                prod_container.innerHTML += `<div class="column" id="uid"  onclick="window.open('product.html?uid=${data[i]['uniqueId']}','_self')">
                <img class="image" src="${data[i]['imageUrl'][0]}">
                <p class="image_text">${data[i]['title']}</p>
                <p class="price"><sup>$</sup>${price}<sup>${decimal}</sup></p>
                </a>
                </div>`
              }
              document.getElementById('loading').style.display = 'none';
              document.getElementById('outer-div').style.display = 'grid';
              pageNumber++;
              let pageDisplay = ""
              let footer_container = document.getElementById("footer-div");
              if ((pageNumber - 1) * 9 < pages) {
                pageDisplay = `Showing ${(pageNumber - 2) * 9 + 1}-${(pageNumber - 1) * 9} of ${pages} products`;
                footer_container.innerHTML = ` <ul class="page">
        <li class="text-footer" onclick="prevPage()"> &lt; </li>
        <li class="text-footer" id="pageNumber" value="${pageNumber}"> ${pageNumber - 1} </li>
        <li class="text-footer" onclick="nextPage()"> &gt; </li>
        <li class="product-text">${pageDisplay}</li></ul>`
              }
              else if (((pageNumber - 2) * 9 + 1 <= pages) && ((pageNumber - 1) * 9 + 1 > pages)) {
                pageDisplay = `Showing ${(pageNumber - 2) * 9 + 1}-${pages} of ${pages} products`;
                footer_container.innerHTML = ` <ul class="page">
        <li class="text-footer" onclick="prevPage()"> &lt; </li>
        <li class="text-footer" id="pageNumber" value="${pageNumber}"> ${pageNumber - 1} </li>
        <li class="text-footer" onclick="nextPage()"> &gt; </li>
        <li class="product-text">${pageDisplay}</li></ul>`
              }
              else {
                pageDisplay = ``;
                prod_container.innerHTML += `</div>
          <img src="Images/error.jpg" width="1000" height="650" class="center">
          </div>`
                footer_container.innerHTML = ` <ul>
        <li class="return-home" onclick="home()">Return to Home</li></ul>`
              }
              document.getElementById('current_page').style.display = 'inline';
            }
            catch (err) {
              alert(err);
            }
          });
        }

        else if ((statusCode < 500) && (statusCode >= 400)) {
          let prod_container = document.getElementById("outer-div");
          prod_container.innerHTML += `</div>
          <img src="Images/error404.png" width="1000" height="650" class="center">
          </div>`
        }

        else if ((statusCode < 600) && (statusCode >= 500)) {
          let prod_container = document.getElementById("outer-div");
          prod_container.innerHTML += `</div>
          <img src="Images/error500.png" width="1000" height="650" class="center">
          </div>`
        }

        else {
          ;
        }
      });
    }, 300)
  }

  else if (catLevel1 != null) {
    document.getElementById('loading').style.display = 'block';
    setTimeout(() => {
      fetch(`http://127.0.0.1:7002/category?cat1=${catLevel1}&cat2=${catLevel2}&page=${pageNumber}&sort=${sortKey}`, {
        method: 'GET',
        mode: 'cors',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Accept': 'application/json',
          'Content-Type': 'application/json;charset=utf-8',

        }

      }).then(response => {
        const statusCode = response.status;
        console.log(statusCode);
        if ((statusCode < 300) && (statusCode >= 200)) {
          response.json().then(data => {
            try {
              if (data === null) throw "Unable to fetch data";
              let pages = data[0]
              let pageTotal = Math.ceil(pages / 9);
              data = data[1];
              let prod_container = document.getElementById("outer-div");
              prod_container.innerHTML = '';
              for (let i = 0; i < data.length; i++) {
                let decimal = (parseFloat(data[i]['price']).toFixed(2)).slice(-2);
                let price = String(parseInt(data[i]['price']));
                prod_container.innerHTML += `<div class="column" name="uid" onclick="window.open('product.html?uid=${data[i]['uniqueId']}','_self')">
              <img class="image" src="${data[i]['Img_URL']}">
              <p class="image_text">${data[i]['Title']}</p>
              <p class="price"><sup>$</sup>${price}<sup>${decimal}</sup></p>
              </a>
            </div>`
              }
              document.getElementById('loading').style.display = 'none';
              document.getElementById('outer-div').style.display = 'grid';
              pageNumber++;
              let pageDisplay = ""
              let footer_container = document.getElementById("footer-div");
              if ((pageNumber - 1) * 9 < pages) {
                pageDisplay = `Showing ${(pageNumber - 2) * 9 + 1}-${(pageNumber - 1) * 9} of ${pages} products`;
                footer_container.innerHTML = ` <ul class="page">
          <li class="text-footer" onclick="prevPage()"> &lt; </li>
          <li class="text-footer" id="pageNumber" value="${pageNumber}"> ${pageNumber - 1} </li>
          <li class="text-footer" onclick="nextPage()"> &gt; </li>
          <li class="product-text">${pageDisplay}</li></ul>`
              }
              else if (((pageNumber - 2) * 9 + 1 <= pages) && ((pageNumber - 1) * 9 + 1 > pages)) {
                pageDisplay = `Showing ${(pageNumber - 2) * 9 + 1}-${pages} of ${pages} products`;
                footer_container.innerHTML = ` <ul class="page">
          <li class="text-footer" onclick="prevPage()"> &lt; </li>
          <li class="text-footer" id="pageNumber" value="${pageNumber}"> ${pageNumber - 1} </li>
          <li class="text-footer" onclick="nextPage()"> &gt; </li>
          <li class="product-text">${pageDisplay}</li></ul>`
              }
              else {
                pageDisplay = ``;
                prod_container.innerHTML += `</div>
            <img src="Images/error.jpg" width="1000" height="650" class="center">
            </div>`
                footer_container.innerHTML = ` <ul>
          <li class="return-home" onclick="home()">Return to Home</li></ul>`
              }

              if ((catLevel2 === 'men') || (catLevel2 === 'women')) {
                catLevel2 = ((catLevel2.charAt(0)).toUpperCase() + catLevel2.slice(1));
                let currentPage_container = document.getElementById("current_page");
                currentPage_container.innerHTML = `Showing Products : ${catLevel2}`;
              }
              else {
                if (catLevel1 === '0') {
                  catLevel1 = "Men"
                }
                else if (catLevel1 === '1') {
                  catLevel1 = "Women"
                }
                else {
                  catLevel1 = "Gift Cards"
                }
                let currentPage_container = document.getElementById("current_page");
                currentPage_container.innerHTML = `Showing Products : ${catLevel1} &rarr; ${catLevel2.replace(/([A-Z])/g, ' $1').trim()}`;
              }
              document.getElementById('current_page').style.display = 'inline';
            }
            catch (err) {
              alert(err);
            }
          });
        }
        else if ((statusCode < 500) && (statusCode >= 400)) {
          let prod_container = document.getElementById("outer-div");
          prod_container.innerHTML += `</div>
        <img src="Images/error404.png" width="1000" height="650" class="center">
        </div>`
        }

        else if ((statusCode < 600) && (statusCode >= 500)) {
          let prod_container = document.getElementById("outer-div");
          prod_container.innerHTML += `</div>
        <img src="Images/error500.png" width="1000" height="650" class="center">
        </div>`
        }

        else {
          ;
        }
      });
    }, 300)
  }
  else {
    if (pageNumber === "") {
      pageNumber = 1;
    }
    document.getElementById('loading').style.display = 'block';
    setTimeout(() => {
      fetch(`http://127.0.0.1:7002/product_query?q=*&page=${pageNumber}&sort=${sortKey}`, {
        method: 'GET',
        mode: 'cors',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Accept': 'application/json',
          'Content-Type': 'application/json;charset=utf-8',

        }

      }).then(response => {
        console.log(response.status);
        const statusCode = response.status;
        if ((statusCode < 300) && (statusCode >= 200)) {
          response.json().then(data => {
            try {
              if (data === null) throw "Unable to fetch data";
              let pages = data[0]
              let pageTotal = Math.ceil(pages / 9);
              data = data[1];
              let prod_container = document.getElementById("outer-div");
              prod_container.innerHTML = '';
              for (let i = 0; i < data.length; i++) {
                let decimal = (parseFloat(data[i]['price']).toFixed(2)).slice(-2);
                let price = String(parseInt(data[i]['price']));
                prod_container.innerHTML += `<div class="column" id="uid"  onclick="window.open('product.html?uid=${data[i]['uniqueId']}','_self')">
                <img class="image" src="${data[i]['imageUrl'][0]}">
                <p class="image_text">${data[i]['title']}</p>
                <p class="price"><sup>$</sup>${price}<sup>${decimal}</sup></p>
                </a>
                </div>`
              }
              document.getElementById('loading').style.display = 'none';
              document.getElementById('outer-div').style.display = 'grid';
              pageNumber++;
              let pageDisplay = ""
              let footer_container = document.getElementById("footer-div");
              if ((pageNumber - 1) * 9 < pages) {
                pageDisplay = `Showing ${(pageNumber - 2) * 9 + 1}-${(pageNumber - 1) * 9} of ${pages} products`;
                footer_container.innerHTML = ` <ul class="page">
      <li class="text-footer" onclick="prevPage()"> &lt; </li>
      <li class="text-footer" id="pageNumber" value="${pageNumber}"> ${pageNumber - 1} </li>
      <li class="text-footer" onclick="nextPage()"> &gt; </li>
      <li class="product-text">${pageDisplay}</li></ul>`
              }
              else if (((pageNumber - 2) * 9 + 1 <= pages) && ((pageNumber - 1) * 9 + 1 > pages)) {
                pageDisplay = `Showing ${(pageNumber - 2) * 9 + 1}-${pages} of ${pages} products`;
                footer_container.innerHTML = ` <ul class="page">
      <li class="text-footer" onclick="prevPage()"> &lt; </li>
      <li class="text-footer" id="pageNumber" value="${pageNumber}"> ${pageNumber - 1} </li>
      <li class="text-footer" onclick="nextPage()"> &gt; </li>
      <li class="product-text">${pageDisplay}</li></ul>`
              }
              else {
                pageDisplay = ``;
                prod_container.innerHTML += `</div>
        <img src="Images/error.jpg" width="1000" height="650" class="center">
        </div>`
                footer_container.innerHTML = ` <ul>
      <li class="return_home" onclick="home()">Return to Home</li>
      </ul>`
              }
            }
            catch (err) {
              alert(err);
            }
          });
        }
        else if ((statusCode < 500) && (statusCode >= 400)) {
          let prod_container = document.getElementById("outer-div");
          prod_container.innerHTML += `</div>
      <img src="Images/error404.png" width="1000" height="650" class="center">
      </div>`
        }

        else if ((statusCode < 600) && (statusCode >= 500)) {
          let prod_container = document.getElementById("outer-div");
          prod_container.innerHTML += `</div>
      <img src="Images/error500.png" width="1000" height="650" class="center">
      </div>`
        }

        else {
          ;
        }

      });
    }, 300)
  }
  let feature_li = document.getElementById("feature_li");
  feature_li.onclick = function () {
    sortedView('');
  }
  let pasc_li = document.getElementById("priceasc_li");
  pasc_li.onclick = function () {
    sortedView('price asc');
  }
  let pdesc_li = document.getElementById("pricedesc_li");
  pdesc_li.onclick = function () {
    sortedView('price desc');
  }
}