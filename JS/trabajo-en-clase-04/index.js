// Declarar una función
function add(number_1, number_2) {
    return number_1 + number_2;
};

function write_me(message, tag="p") {
    return document.write(`<${tag}>${message}</${tag}>`);
};

// Funciones closure.
function calc(number_1, number_2, operator="-"){
    function substract() {
        return number_1 - number_2;
    };
    function division() {
        return number_1 / number_2;
    };

    if (operator === "-") {
        return substract();
    } else if (operator === "/") {
        return number_1 / number_2;
    } else {
        return null
    };
};

// Funciones callback
function get_fullname(first_name, last_name) {
    return `${first_name} ${last_name}`;
};

function greet(first_name, last_name, callback) {
    return "¡Hola! " + callback(first_name, last_name);
};
 
// Invocar una función
write_me("Exploraremos funciones simples, arrow, closure, clallbacks y recursivas.");
write_me("Funciones Simples", "h2");
document.write(`<p>La suma de 2 + 2 es ${add(2, 2)}</p>`);


// Arrow function o funciones flecha
write_me("Funciones Arrow 💘", "h2");
let product = (number_1, number_2) => { number_1 * number_2 };
document.write(`<p>La multiplicación de 3 * 7 es ${product(3, 7)}</p>`);

// Invocar una función closure.
write_me("Funciones Closure", "h2");
write_me(`Resultado de calc(4, 3, "-") = ${calc(4,3, "-")}`);

// Invocar el callback
write_me("Funciones Callback", "h2");
write_me(greet("Agustín", "Comolli", get_fullname));