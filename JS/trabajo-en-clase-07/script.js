/**
 * Obtiene información sobre una provincia a través de una solicitud a la API de georef.
 * @param {string} province - El nombre de la provincia que se desea buscar.
 * @returns {Promise} - Una promesa que se resuelve con los datos de la provincia o se rechaza en caso de error.
 */
function getProvince(province) {
    return fetch(`https://apis.datos.gob.ar/georef/api/provincias?nombre=${province}`)
        .then(response => response.json())
        .catch(error => console.log(error));
}

/**
 * Maneja la búsqueda de una provincia cuando se envía un formulario.
 * @param {Event} event - El evento de envío del formulario.
 */
async function searchProvince(event) {
    // Evitar que se recargue la página.
    event.preventDefault();

    // Obtener el nombre de la provincia ingresado por el usuario.
    const province = document.querySelector("#province").value;

    // Seleccionar el elemento de mensaje en el HTML.
    const message = document.querySelector(".message");

    // Realizar una solicitud asincrónica para obtener información sobre la provincia.
    const infoProvince = await getProvince(province);

    // Validar si el campo de provincia está vacío.
    if (!province) {
        message.innerHTML = "<p>Debe ingresar una provincia</p>";
        return;
    } else {
        // Verificar si se encontraron provincias coincidentes en la respuesta.
        if (infoProvince.provincias.length > 0) {
            // Recorrer y mostrar las provincias encontradas.
            let provinces = infoProvince.provincias;
            for (let provinceFound of provinces) {
                message.innerHTML += `<p>${provinceFound.nombre}</p>`;
            };
        };
    };
}
