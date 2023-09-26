// Números aleatorios


// Obtenemos un número al azar entre [0, 1) con 16 decimales
let random_number = Math.random();

// Multiplicamos dicho número por el valor máximo que buscamos (5)
random_number = random_number * 5;

// Redondeamos inferiormente, quedándonos sólo con la parte entera
random_number = Math.floor(random_number);

console.log(random_number);