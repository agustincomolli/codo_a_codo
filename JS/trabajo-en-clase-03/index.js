let sum = 0;
let not_finished = true;

while (not_finished) {
   sum += parseInt(prompt("Ingrese un número: "));
   if (!confirm("¿Dese continuar?")) {
    not_finished = false;
   }
};

document.write("<p>La suma es: " + sum + "</p>");