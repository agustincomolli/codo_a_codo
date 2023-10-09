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


function read_notes() {
    let note = 0;
    let count = 0;
    total = 0;

    note = parseInt(prompt("Ingrese un número:"));
    while (note !== -1) {
        count ++;
        total += note;
        note = parseInt(prompt("Ingrese un número:"));
    };

    return total / count;
};


let average = read_notes();

write_me(`El promedio de notas es: ${average}`);