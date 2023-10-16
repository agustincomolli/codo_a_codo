/**
 * Escribe un mensaje en el documento HTML dentro de un elemento HTML especificado.
 *
 * @param {string} message - El mensaje que se va a escribir en el documento HTML.
 * @param {string} [tag="p"] - La etiqueta HTML en la que se debe envolver el mensaje.
 * @returns {void} - No retorna ningún valor, ya que solo escribe en el documento HTML.
 */
function write_me(message, tag="p", className = "message") {
    // Genera el contenido HTML con la etiqueta especificada y el mensaje.
    const htmlContent = `<${tag} class='${className}'>${message}</${tag}>`;

    // Escribe el contenido HTML en el documento.
    document.write(htmlContent);
};


function isValidDay(day) {
    if (day >= 1 && day <= 31) {
        return true;
    }
};


function isValidMonth(month) {
    if (month >= 1 && month <= 12) {
        return true;
    }
};


function isValidYear(year) {
    if (year >= 1 && year < 3000) {
        return true;
    }
};


function isYearLeap(year) {
    if (year < 1582) {
        return false;
    };
    if (year % 4 != 0) {
        return false;
    } else if (year % 100 != 0) {
        return true;
    } else if (year % 400 != 0) {
        return false;
    } else {
        return true;
    }
};


function getDaysOfMonth(month, isYearLeap) {
    if ([1, 3, 5, 7, 8, 10, 12].includes(month)) {
        return 31;
    } else if (month === 2 && isYearLeap) {
        return 29;
    } else if (month === 2 && !isYearLeap) {
        return 28
    } else {
        return 30;
    };
};


let userDate = prompt("Ingrese una fecha en formato (dd-MM-yyyy);");
userDateSplited = userDate.split("-");
let day = parseInt(userDateSplited[0]);
let month = parseInt(userDateSplited[1]);
let year = parseInt(userDateSplited[2])

if (isValidDay(day) && isValidMonth(month) && isValidYear(year)) {
    let lastDayOfMonth = getDaysOfMonth(month, isYearLeap(year));
    write_me(`El último día del mes de su fecha (${userDate}) es el <strong>${lastDayOfMonth}</strong>.`)
} else {
    write_me("No ha ingresado una fecha correcta. Recargue la página y pruebe de nuevo.", "p", "warning");
};