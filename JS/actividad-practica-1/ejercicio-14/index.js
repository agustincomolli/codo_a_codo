let number = parseInt(prompt("Ingrese un número: "));
let answer = [];

if (number % 2 === 0) {
    answer.push(2);
};

if (number % 3 === 0) {
    answer.push(3);
};

if (number % 5 === 0) {
    answer.push(5);
};

if (number % 7 === 0) {
    answer.push(7);
};

if (answer.length === 0){
    answer.push("ninguno")
};

for (let index = 0; index < answer.length; index++) {
    document.write("<p>El número es divisible por <strong>" + answer[index] + "</strong></p>");
};