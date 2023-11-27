const URL = "http://192.168.100.13:5000"
const formAddNew = document.querySelector("#add-new")

formAddNew.addEventListener("submit", e => {
    e.preventDefault();
    const formData = new FormData(formAddNew);
    const response = fetch(URL + "/products", {
        method: "POST",
        body: formData
    }).then(res => res.json())
        .then(data => {
            console.log(data);
            alert('Producto agregado correctamente');
            window.location.href = 'index.html'
        })
})