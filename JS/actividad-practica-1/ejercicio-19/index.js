let calification = parseInt(prompt("¿Qué nota te sacaste?"));
let answer = "";

if (calification > 0 && calification < 4) {
    answer = "Muy deficiente";
} else if (calification > 4 && calification < 6) {
    answer = "Insuficiente";
} else if (calification > 5 && calification < 7) {
    answer = "Suficiente";
} else if (calification > 6 && calification < 8) {
    answer = "Bien";
} else if (calification === 8) {
    answer = "Notable";
} else if (calification > 8 && calification < 11) {
    answer = "Sobresaliente";
} else {
    answer = "Nota errónea";
};

document.write(`<p>${answer}</p>`)