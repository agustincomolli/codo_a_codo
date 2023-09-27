let number_1 = parseInt(prompt("Ingrese el 1° número:"));
let number_2 = parseInt(prompt("Ingrese el 2° número:"));
let number_3 = parseInt(prompt("Ingrese el 3° número:"));
let greater = 0;

if (number_1 > number_2 && number_1 > number_3) {
    greater = number_1;
} else if(number_2 > number_3) {
    greater = number_2;
} else {
    greater = number_3;
};

document.write("<p>El número más grande es el " + greater + "</p>");