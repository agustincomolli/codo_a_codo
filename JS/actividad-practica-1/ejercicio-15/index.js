let number = parseInt(prompt("Ingrese un número: "));


document.write("<h3>Has ingresado " + number + "</h3>")

for (let index = 0; index < number; index++) {
    if (number % index === 0) {
        document.write("<p>El número es divisible por <strong>" + index + "</strong></p>")
    };
};