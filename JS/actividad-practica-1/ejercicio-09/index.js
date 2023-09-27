let phrase = prompt("Escriba algo:");
let count = 0;

for (let char of phrase) {
    if (char === "a") { count++ };
};

document.write("<p>Tu frase es: '" + phrase + "'</p>");
document.write("<p>Hay " + count + " letras 'a' en esa frase.</p>");