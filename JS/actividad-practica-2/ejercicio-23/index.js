/**
 * Escribe un mensaje en el documento HTML dentro de un elemento HTML especificado.
 *
 * @param {string} message - El mensaje que se va a escribir en el documento HTML.
 * @param {string} [tag="p"] - La etiqueta HTML en la que se debe envolver el mensaje.
 * @param {string} [className="message"] - La clase CSS para poder aplicarle estilos.
 * @returns {void} - No retorna ningún valor, ya que solo escribe en el documento HTML.
 */
function writeMe(message, tag = "p", className = "message") {
    // Genera el contenido HTML con la etiqueta especificada y el mensaje.
    const htmlContent = `<${tag} class='${className}'>${message}</${tag}>`;

    // Escribe el contenido HTML en el documento.
    document.write(htmlContent);
};


function getElement(array, index) {
    if (index < 0 || index >= array.length) {
        writeMe("El índice está fuera de rango","p", "warning");
        return false;
    };
    if (array == []) {
        writeMe("El array está vacío","p", "warning");
        return false;
    }
    return array[index];
}


let numbers = [46, 65, 19, 53, 38, 24, 33, 28];
let index = parseInt(prompt("Ingrese el índice del elemento que quiere obtener:"));

writeMe(`Los números del array son: ${numbers}`, "p", "");
writeMe(`El índice ingresado es ${index}`, "p", "");
let element = getElement(numbers, index);
if (element != false) {
    writeMe(`El valor buscado es ${element}`);
}