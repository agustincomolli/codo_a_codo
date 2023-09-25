// Tipos de datos

// Strings
let my_name = "Agustín";
console.log("La variable my_name es de tipo", typeof my_name);

// Numbers
let my_age = 46;
console.log("La variable my_age es de tipo", typeof my_age);

let my_height = 1.62;
console.log("La variable my_height es de tipo", typeof my_height);

// Booleans
let have_children = false;
console.log("La variable have_children es de tipo", typeof have_children);

// Objects
let my_data = {
    name: "Agustín",
    age: 46,
    height: 1.62,
    have_children: false
};
console.log("La variable my_data es de tipo", typeof my_data);

console.log("\nNombre:",my_data.name);
console.log("Edad:",my_data.age);
console.log("Altura:",my_data.height);
console.log("¿Tiene hijos?",my_data.have_children);

// Arrays
let my_favourites_foods = ["cordero al asador", "guiso de lentejas", "empanadas", "pizzas"];
console.log("\nLa variable my_favourites_foods es de tipo", typeof my_favourites_foods);
console.log("Mi comida favorita ganadora es:", my_favourites_foods[0]);
console.log(my_name, "tiene", my_favourites_foods.length, "comidas favoritas");

// Conversión a números enteros
let my_float = 3.57;
let my_integer = parseInt(my_float);
console.log("\nmy_float =", my_float, "es ahora:", my_integer);
let my_string = "1977";
my_integer = parseInt(my_string);
console.log("my_float = '1977'", "es ahora:", my_integer);

// Conversión a números flotantes
my_string = "10";
my_float = parseFloat(my_string);
console.log("\nmy_string = '" + my_string + "' es ahora:", my_float);

// Conversión a string
my_string = String(my_integer);
console.log("\nmy_integer =", my_integer, "es ahora:'" + my_string + "'")