const vowels = ["a", "e", "i", "o", "u"];
let phrase = prompt("Escriba una frase:");
let appears = "";

for (let char of phrase) {
    if (vowels.includes(char)) {
        appears += char;
    };
};

document.write("<p>Tu frase es: '" + phrase + "'</p>");
document.write("<p>Las vocales que aparecen son: <strong>" + appears + "</strong></p>");