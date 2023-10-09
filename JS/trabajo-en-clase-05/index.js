/**
 * Escribe un mensaje en el documento HTML dentro de un elemento HTML especificado.
 *
 * @param {string} message - El mensaje que se va a escribir en el documento HTML.
 * @param {string} [tag="p"] - La etiqueta HTML en la que se debe envolver el mensaje.
 * @returns {void} - No retorna ningún valor, ya que solo escribe en el documento HTML.
 */
function write_me(message, tag = "p") {
    // Genera el contenido HTML con la etiqueta especificada y el mensaje.
    const htmlContent = `<${tag}>${message}</${tag}>`;

    // Escribe el contenido HTML en el documento.
    document.write(htmlContent);
}


let car = {
    patent: "AC 134 DD"
};

let tennis_player = {
    first_name: "Roger",
    last_name: "Federer",
    age: 40,
    saludar: () => `Hola me llamo ${tennis_player.first_name}`
};

write_me(tennis_player.saludar());

function Car(brand, model) {
    this.brand = brand;
    this.model = model;
};

let my_car = new Car("Fiat", "Palio Adventure");
write_me(`Mi auto es un ${my_car.brand} ${my_car.model}`);


// Manipulación del DOM
let header = document.querySelector("h1").innerHTML += " y Manipulación del DOM";

write_me("Manipulando el DOM", "h2");

// Seleccionar todos los párrafos y cambiarles la clase.
let paragraphs = document.querySelectorAll("p");
for (paragraph of paragraphs) {
    paragraph.classList.toggle("code");
};

// Agregar una clase a una etiqueta;
let subtitle = document.querySelector("h2");
subtitle.classList.toggle("subtitle-1");

// Seleccionar las etiquetas con un estilo.
subtitles = document.getElementsByClassName("subtitle-1");
for (subtitle of subtitles) {
    subtitle.classList.toggle("subtitle-2");
};

document.querySelector("title").innerHTML = "Cambios";

let task_list = [];

function show_tasks(task) {
    let tasks = document.getElementById("tasks")
    let list_item = document.createElement("li");
    list_item.innerHTML = task;
    tasks.appendChild(list_item);
};


function add_task() {
    let new_task = document.getElementById("task").value;
    new_task = new_task.trim()
    task_list.push(new_task);
    show_tasks(new_task);
    document.getElementById("task").value = "";
};