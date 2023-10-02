let phrase = prompt("Escriba una frase:");
let total_vowels = [0, 0, 0, 0, 0];

for (let char of phrase) {
    switch (char) {
        case "a":
            total_vowels[0]++;
            break;
        case "e":
            total_vowels[1]++;
            break;
        case "i":
            total_vowels[2]++;
            break;
        case "o":
            total_vowels[3]++;
            break;
        case "u":
            total_vowels[4]++;
            break;
        default:
            break;
    };
};

for (let index in total_vowels) {
    let char = "";
    switch (parseInt(index)) {
        case 0:
            char = "a";
            break;
        case 1:
            char = "e";
            break;
        case 2:
            char = "i";
            break;
        case 3:
            char = "o";
            break;
        case 4:
            char = "u";
            break;
        default:
            break;
    };

    document.write("<p>" + char + " = " + total_vowels[index] + "</p>");
};