let number_1 = parseInt(prompt("Ingrese el 1° número:"));
let number_2 = parseInt(prompt("Ingrese el 2° número:"));
let greater = number_1 > number_2 ? number_1 : number_2;

document.write("<p>El número más grande es el " + greater + "</p>")