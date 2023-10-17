/**
 * Escribe un mensaje en el documento HTML dentro de un elemento HTML especificado.
 *
 * @param {string} message - El mensaje que se va a escribir en el documento HTML.
 * @param {string} [tag="p"] - La etiqueta HTML en la que se debe envolver el mensaje.
 * @param {string} [className="message"] - La clase CSS para poder aplicarle estilos.
 * @returns {void} - No retorna ningún valor, ya que solo escribe en el documento HTML.
 */
function writeMe(message, tag = "p") {
    // Genera el contenido HTML con la etiqueta especificada y el mensaje.
    const htmlContent = `<${tag}>${message}</${tag}>`;

    // Escribe el contenido HTML en el documento.
    document.write(htmlContent);
}


function cleanMessages() {
    if (document.querySelector(".warning") != null) {
        document.querySelector(".warning").remove()
    };
    if (document.querySelector(".answer") != null) {
        document.querySelector(".answer").remove();
    };
};


function isValidInput(input) {
    let month = input;
    if (!(month >= 1 && month <= 12)) {
        const warning = document.createElement("h3");
        warning.className = "warning";
        warning.textContent = "El número ingresado no corresponde a un número de mes válido.";
        results.appendChild(warning);
        return false;
    } else {
        return true;
    };
};

function getDaysOfMonth(month) {
    if ([1, 3, 5, 7, 8, 10, 12].includes(month)) {
        return 31;
    } else if (month === 2) {
        return 28;
    } else {
        return 30;
    };
};


function showDaysOfMonth() {
    let month = parseInt(inputMonth.value);

    cleanMessages();
    
    if (isValidInput(month)) {
        let daysOfMonth = getDaysOfMonth(month);
        const answer = document.createElement("p");
        answer.className = "answer"
        answer.innerHTML = `El mes ${month} tiene ${daysOfMonth} días`;
        results.appendChild(answer);
    }
};


const results = document.querySelector(".results");
const inputMonth = document.querySelector("#month");
const btnSend = document.querySelector("#send");

btnSend.addEventListener("click", showDaysOfMonth);
