// Mostrar información al usuario.
alert("¡Hola mundo!");

// Pedir información.
let user_name = prompt("¿Cómo te llamas?");

// Pedir confirmación al usuario.
let can_continue = confirm("¿" + user_name + " deseas continuar?");
if (can_continue) {
    document.write("<h2>¡Bienvenido " + user_name + "!</h2>");
} else {
    window.close();
};

let age = parseInt(prompt("¿Cuántos años tienes?"));
let result = ";"

switch (true) {
    case age <= 12:
        result = "niño";
        break;
    case age < 18:
        result = "adolescente";
        break;
    case age < 65:
        result = "adulto";
        break;
    default:
        result = "viejo";
        break;
};
document.write("<p>Tienes " + age + " y eres un " + result);