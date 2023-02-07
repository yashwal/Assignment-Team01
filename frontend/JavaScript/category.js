function generateCategory() {
  fetch(`http://127.0.0.1:7002/categoryTree`, {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Accept': 'application/json',
      'Content-Type': 'application/json;charset=utf-8',

    }

  }).then(response => response.json()).then(data => {
    try {
      if (data === null) throw "Unable to fetch data";
      let cat1 = data[0];
      let cat2 = data[1];
      let cat3 = data[2];
      let cat_container = document.getElementById("dropdownheader");
      cat_container.innerHTML = ``;
      for (let i = 0; i < cat1.length; i++) {
        let catId = cat1[i][1];
        let catValue = cat1[i][0];
        let value = cat1[i][0];
        if (catValue != 'exp') {
          let dataElement = data[parseInt(catId) + 1];
          let elementArr = dataElement[catId];
          var tempo = ``;
          for (let j = 0; j < elementArr.length; j++) {
            let valueName = elementArr[j].replace(/([A-Z])/g, ' $1').trim();
            tempo += `<li onclick="getCategory('${catId}','${elementArr[j]}')" class="hover-button">${valueName}</li>`;
          }
        }
        if (catValue == 'exp') {
          value = 'Others';
          cat_container.innerHTML += `<div class="right-menu">
        <button class="button" onclick="getCategory('${catId}','${value}')">Gift Cards</button>
        </div>`;
        }
        else {
          cat_container.innerHTML += `<div class="right-menu">
      <button class="button" onclick="getCategory('${catId}',value)" value="${value}">${catValue}</button>
      <div class="dropdown-menu">` + tempo;
        }
      }
    }
    catch (err) {
      alert(err);
    }
  });
};

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

export { generateCategory,sortedView };