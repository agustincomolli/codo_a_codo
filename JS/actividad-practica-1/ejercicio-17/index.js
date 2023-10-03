let number = parseInt(prompt("Ingrese un número: "));
let answer = "es";

if (number < 2) {
    answer = "no es";
} else {
    for (let count = 2; count < number; count++) {
        if (number % count === 0) {
            answer = "no es"
            break;
        };
    };
};



document.write(`<p>El número ${number} ${answer} número primo.</p>`)