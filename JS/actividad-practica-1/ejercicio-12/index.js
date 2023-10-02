let phrase = prompt("Escriba una frase:");
let total_vowels = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0,
};

for (let char of phrase) {
    if ("aeiou".includes(char.toLowerCase())) {
        total_vowels[char]++;
    };
};

for (let char in "aeiou") {
    document.write("<p>" + char + ": " + total_vowels[char] + "</p>");
};