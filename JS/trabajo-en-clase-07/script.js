const formSearch = document.querySelector("#search");

function getProvinces() {
    return fetch(`https://apis.datos.gob.ar/georef/api/provincias`)
        .then(response => response.json())
        .catch(error => console.log(error));
}


async function fillProvincesSelector() {
    const provincesSelector = document.querySelector("#provinces");
    const infoProvinces = await getProvinces();

    if (infoProvinces.provincias.length > 0) {
        let provinces = infoProvinces.provincias;
        provinces.sort((a, b) => a.nombre.localeCompare(b.nombre));
        for (let province of provinces) {
            const optionProvince = document.createElement("option");
            optionProvince.text = province.nombre;
            provincesSelector.appendChild(optionProvince);
        };

    };
};


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

    // Deshabilitar el botón y mostrar el estado de trabajo.
    const btnSearch = document.querySelector("#btn-search");
    btnSearch.toggleAttribute("disabled");
    btnSearch.setAttribute("aria-busy", "true");

    // Realizar una solicitud asincrónica para obtener información sobre la provincia.
    const infoProvince = await getProvince(province);

    // Validar si el campo de provincia está vacío.
    if (!province) {
        message.innerHTML = "<p>Debe ingresar una provincia</p>";
    } else {
        // Verificar si se encontraron provincias coincidentes en la respuesta.
        if (infoProvince.provincias.length > 0) {
            // Recorrer y mostrar las provincias encontradas.
            let provinces = infoProvince.provincias;
            for (let provinceFound of provinces) {
                message.innerHTML += `<p>${provinceFound.nombre}</p>`;
            };
        } else {
            message.innerHTML = "<p>No se encontró ninguna provincia</p>"
        };
    };
    // Habilitar el botón y quitar el estado de trabajo.
    btnSearch.toggleAttribute("disabled");
    btnSearch.removeAttribute("aria-busy");
}


formSearch.addEventListener("submit", searchProvince);
fillProvincesSelector();