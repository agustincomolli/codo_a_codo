/**
 * Escribe un mensaje en el documento HTML dentro de un elemento HTML especificado.
 *
 * @param {string} message - El mensaje que se va a escribir en el documento HTML.
 * @param {string} [tag="p"] - La etiqueta HTML en la que se debe envolver el mensaje.
 * @param {string} [className="message"] - La clase CSS para poder aplicarle estilos.
 * @returns {void} - No retorna ningún valor, ya que solo escribe en el documento HTML.
 */
function writeMe(message, tag="p", className = "message") {
    // Genera el contenido HTML con la etiqueta especificada y el mensaje.
    const htmlContent = `<${tag} class='${className}'>${message}</${tag}>`;

    // Escribe el contenido HTML en el documento.
    document.write(htmlContent);
};


function invertNumber(number) {
    let stringNumber = number.toString();
    let arrayNumber = [];
    for (let char of stringNumber) {
        arrayNumber.unshift(char);
    };
    stringNumber = arrayNumber.join("");
    return parseInt(stringNumber);
};


let number = parseInt(prompt("Ingrese un número:"));

writeMe(`El número invertido es ${invertNumber(number)}`);