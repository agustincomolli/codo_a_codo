/**
 * Escribe un mensaje en el documento HTML dentro de un elemento HTML especificado.
 *
 * @param {string} message - El mensaje que se va a escribir en el documento HTML.
 * @param {string} [tag="p"] - La etiqueta HTML en la que se debe envolver el mensaje.
 * @returns {void} - No retorna ningún valor, ya que solo escribe en el documento HTML.
 */
function writeMe(message, tag="p", className = "message") {
    // Genera el contenido HTML con la etiqueta especificada y el mensaje.
    const htmlContent = `<${tag} class='${className}'>${message}</${tag}>`;

    // Escribe el contenido HTML en el documento.
    document.write(htmlContent);
};


function promedio3(num_1, num_2, num_3) {
    return (num_1 + num_2 + num_3) / 3;
};


let number_1 = parseInt(prompt("Ingrese el 1° número:"));
let number_2 = parseInt(prompt("Ingrese el 2° número:"));
let number_3 = parseInt(prompt("Ingrese el 3° número:"));

writeMe(`El promedio de los tres números es: ${promedio3(number_1, number_2, number_3)}`);