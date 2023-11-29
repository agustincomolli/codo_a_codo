/**
 * Este código gestiona la presentación de un formulario y la posterior
 * publicación de los datos del formulario en un servidor usando Fetch API.
 */

// URL del endpoint donde se enviarán los datos del formulario. Asegúrate de tener el servidor corriendo en esta dirección.
const URL = "http://192.168.100.13:5000";

// Selecciona el formulario en el documento con el ID 'add-new'.
const formAddNew = document.querySelector("#add-new");

// Añade un 'event listener' para el evento de tipo 'submit' en el formulario.
formAddNew.addEventListener("submit", e => {
    // Previene el comportamiento predeterminado del formulario que causaría una recarga de la página.
    e.preventDefault();

    // Crea un objeto FormData basado en el formulario actual - esto permite recoger fácilmente todos los valores del formulario.
    const formData = new FormData(formAddNew);

    // Ejecuta la solicitud Fetch asumiendo que el servidor en `URL` va a aceptar esta petición con el cuerpo del formulario.
    fetch(URL + "/products", {
        method: "POST", // Indica que es una solicitud de tipo POST.
        body: formData  // Adjunta los datos del formulario como el cuerpo de la solicitud.
    })
        .then(res => {
            // Se comprueba que la promesa no ha sido rechazada y que se haya completado con un estado HTTP válido.
            if (!res.ok) {
                // Lanza un error con la respuesta no exitosa, esto causará que la ejecución salte al bloque 'catch'.
                throw new Error(`Network response was not ok, the status is ${res.status}`);
            }
            return res.json(); // Si la respuesta es satisfactoria, procesa la respuesta como JSON.
        })
        .then(data => {
            // Maneja la data procesada - aquí simplemente la registramos en la consola y mostramos una alerta al usuario.
            console.log(data);
            alert('Producto agregado correctamente');
            window.location.href = 'index.html'; // Redirecciona al usuario a 'index.html'.
        })
        .catch(error => {
            // Maneja cualquier error que ocurra durante la solicitud o el procesamiento de la respuesta.
            console.error('There has been a problem with your fetch operation:', error);
        });
});

