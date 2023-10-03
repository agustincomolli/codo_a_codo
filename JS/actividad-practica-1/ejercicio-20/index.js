let text = "";
let all_text = "";
let want_continue = true;

while (want_continue) {
    text = prompt("Ingrese un texto:");
    all_text += text + "-"
    want_continue = confirm("¿Desea continuar?")
};

document.write("<p>" + all_text + "</p>");