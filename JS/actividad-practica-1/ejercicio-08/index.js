let number = parseInt(prompt("Ingrese un número:"))
let is_divisible = number % 2 === 0 ? "<strong>es</strong>" : "<strong>no es</strong>";

document.write("<p>El número " + is_divisible + " divisible por 2</p>");