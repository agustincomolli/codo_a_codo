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


function sortText(text) {
    let listOfChars = [];
    for (let char of text) {
        listOfChars.push(char);
    };
    let orderedChars = listOfChars.sort();
    let orderedText = ""
    for (char of orderedChars) {
        orderedText += char;
    };
    return orderedText;
};


let userInput = prompt("Escriba una palabra o frase:");
let sortedText = sortText(userInput);
writeMe(`Tu palabra o frase es: ${userInput}.`);
writeMe(`De forma ordenada es: ${sortedText}`);