/**
 * Escribe un mensaje en el documento HTML dentro de un elemento HTML especificado.
 *
 * @param {string} message - El mensaje que se va a escribir en el documento HTML.
 * @param {string} [tag="p"] - La etiqueta HTML en la que se debe envolver el mensaje.
 * @returns {void} - No retorna ningún valor, ya que solo escribe en el documento HTML.
 */
function write_me(message, tag="p") {
    // Genera el contenido HTML con la etiqueta especificada y el mensaje.
    const htmlContent = `<${tag}>${message}</${tag}>`;

    // Escribe el contenido HTML en el documento.
    document.write(htmlContent);
}

function double(number) {
    return number * 2;
};


function square(number) {
    return number**2;
};


function next(number){
    return ++number;
};


function print_double_next(number) {
    next_number = next(number)
    write_me(`Tu número es ${number}`, "h2");
    write_me(`El doble del número siguiente es ${double(next_number)}`);
}


let my_number = parseInt(prompt("Ingrese un número:"));
print_double_next(my_number);