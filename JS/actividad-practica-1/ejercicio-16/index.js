let number_1 = parseInt(prompt("Ingrese el número 1:"));
let number_2 = parseInt(prompt("Ingrese el número 2:"));
let number_1_divisors = [];
let number_2_divisors = [];
let common_divisors = [];

// Encontrar los divisores del número 1.
for (let index = 2; index <= number_1; index++) {
    if (number_1 % index === 0) {
        number_1_divisors.push(index);
    };
};

// Encontrar los divisores del número 2.
for (let index = 2; index <= number_2; index++) {
    if (number_2 % index === 0) {
        number_2_divisors.push(index);
    };
};

// Encontrar los divisores comunes.
for (let index = 0; index < number_1_divisors.length; index++) {
    if (number_2_divisors.includes(number_1_divisors[index])) {
        common_divisors.push(number_1_divisors[index]);
    };
};

// Mostrar el resultado.
if (common_divisors.length > 0) {
    document.write("<h3>Los divisores comunes a " + number_1 + " y " + number_2 + " son:</h3>");
    for (let divisor of common_divisors) {
        document.write("<p> 👉 " + divisor + "</p>");
    };
} else {
    document.write("<p>No existe ningún divisor común.</p>");
}