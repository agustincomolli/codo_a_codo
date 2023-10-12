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


function area(radius) {
    return Math.PI * radius * radius;
};


let radius = parseFloat(prompt("Ingrese el radio del círculo:"));
write_me(`El área del círculo es ${area(radius)}`);

function addMessage(textToSpeak) {
    const message = new SpeechSynthesisUtterance(textToSpeak);
    speechSynthesis.speak(message);
};


const btnSpeak = document.querySelector(".speak");
btnSpeak.addEventListener("click", ()=>{
    addMessage("¡La puta que lo parió!");
    addMessage("Que cagada");
});
