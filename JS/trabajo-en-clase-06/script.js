function createCard(title, imageURL){
    let card = document.createElement("div");
    let image = document.createElement("img");
    let cardTitle = document.createElement("span");
    
    card.className = "card";
    image.src = imageURL;
    card.appendChild(image);
    cardTitle.innerHTML = title;
    card.appendChild(cardTitle);
    
    return card;
};


function displayPictures(json) {
    const results = document.querySelector("#results");
    for (let i = 0; i < 10; i++) {
        let card = createCard(json[i].title, json[i].thumbnailUrl);
        results.appendChild(card);
    };
};


function searchData() {
    const apiURL = "https://jsonplaceholder.typicode.com/photos";
    // Función asincrónica de JS que hace peticiones a APIs.
    fetch(apiURL)
        .then(response => response.json())
        .then(json => displayPictures(json))
};


const searchButton = document.querySelector("#search-btn");
searchButton.addEventListener("click", searchData);