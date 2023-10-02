let number = parseInt(prompt("Ingrese un número: "));
let answer = null;

if (number % 2 === 0) {
    answer = 2;
} else if (number % 3 === 0) {
    answer = 3;
} else if (number % 5 === 0) {
    answer = 5;
} else if (number % 7 === 0) {
    answer = 7;
} else {
    answer = "ninguno"
}

document.write("<p>El número es divisible por <strong>" + answer + "</strong></p>")