let dni_number = 0;
let want_continue = true;
let letters = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N",
    "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"];

while (want_continue) {
    let result_division = 0;
    let message = "";

    dni_number = parseInt(prompt("Ingrese un DNI:"));
    if (typeof dni_number == NaN || dni_number < 1 || dni_number > 99999999) {
        alert("El valor ingresado no es correcto.");
    } else {
        result_division = dni_number % 23;
        message = `Al DNI ${dni_number} le corresponde la letra ${letters[result_division]}`;
        alert(message);
        document.write("<p>" + message + "</p>");
    };

    want_continue = confirm("¿Desea continuar?");
};