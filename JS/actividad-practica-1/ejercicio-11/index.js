const VOWELS = ["a", "e", "i", "o", "u"];
let phrase = prompt("Escriba una frase:");
let count = 0;

for (let char of phrase) {
    if (VOWELS.includes(char)) {
        count++;
    };
};

document.write("<p>Su frase:</p>");
document.write("<p><em>'" + phrase + "'</em></p>");
document.write("<p>Tiene "+ count + " vocales</p>");