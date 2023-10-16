/**
 * Escribe un mensaje en el documento HTML dentro de un elemento HTML especificado.
 *
 * @param {string} message - El mensaje que se va a escribir en el documento HTML.
 * @param {string} [tag="p"] - La etiqueta HTML en la que se debe envolver el mensaje.
 * @returns {void} - No retorna ningún valor, ya que solo escribe en el documento HTML.
 */
function writeMe(message, tag = "p") {
    // Genera el contenido HTML con la etiqueta especificada y el mensaje.
    const htmlContent = `<${tag}>${message}</${tag}>`;

    // Escribe el contenido HTML en el documento.
    document.write(htmlContent);
}


function isValidDay(day) {
    if (day >= 1 && day <= 31) {
        return true;
    } else {
        return false;
    };
};


function isValidMonth(month) {
    if (!(month >= 1 && month <= 12)) {
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


let userDate = prompt("Ingrese una fecha en formato (dd-MM-yyyy);");
userDateSplited = userDate.split("-");
let day = parseInt(userDateSplited[0]);
let month = parseInt(userDateSplited[1]);

if (isValidDay(day) && isValidMonth(month)) {
    let days = getDaysOfMonth(month);
    writeMe(`El mes de su fecha (${userDate}) tiene ${days} días.`)
} else {
    writeMe("No ha ingresado una fecha correcta. Recargue la página y pruebe de nuevo.");
};