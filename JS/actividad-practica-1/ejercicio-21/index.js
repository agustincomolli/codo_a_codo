let number;
let want_continue = true;
let total = 0;

while (want_continue) {
    number = parseInt(prompt("Ingrse un número:"));
    if (typeof number == NaN) {
        alert("¡No es un número!");
    };
    total += number;
    want_continue = confirm("¿Desea continuar?");
};

document.write(`<p>La suma de los números ingresados es ${total}</p>`)