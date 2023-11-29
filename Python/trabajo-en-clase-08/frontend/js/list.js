// Define la URL del endpoint para la solicitud fetch.
const URL = "http://192.168.100.13:5000";

// Realiza una solicitud fetch a la URL de los productos.
fetch(URL + "/products")
    .then(response => {
        // Verifica si la respuesta de la solicitud es exitosa.
        if (!response.ok) {
            // Si no es exitosa, lanza un error con el estado de la respuesta HTTP.
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        // Si la respuesta es exitosa, la procesa y convierte en JSON.
        return response.json();
    })
    .then(data => {
        // Una vez convertida la respuesta en JSON, imprime la data para inspección.
        console.log(data);
        // Inicia una cadena HTML vacía para ser llenada con el contenido.
        let html = "";
        // Itera a través del array de datos y concatena la información de cada producto.
        data.forEach(product => {
            // Usa plantillas literales para incluir dinámicamente los valores en la cadena HTML.
            html += `<tr>
                <td>${product.id}</td>
                <td>${product.name}</td>
                <td>${product.price}</td>
                <td>${product.stock}</td>
                <td><button class="edit-product">✏️</button></td>
                <td><button class="delete-product" data-id="${product.id}">❌</button></td>
            </tr>`;
        });
        // Inserta el HTML resultante en el elemento con el id 'products'.
        document.querySelector("#products").innerHTML = html;
    })
    .catch(error => {
        // Captura y registra cualquier error que ocurra durante la solicitud fetch.
        console.error('Error fetching data: ', error);
        // Aquí puedes agregar manejo de errores, como mostrar un mensaje de error en la interfaz.
    });


document.querySelector("#products").addEventListener("click", (e) => {
    // Verificar si el botón de borrado fue clickeado utilizando la delegación de eventos
    if (e.target && e.target.classList.contains('delete-product')) {
        // Obtener el ID del producto del atributo 'data-id'
        const productId = e.target.getAttribute('data-id');
        // Llamar a deleteProduct pasando el ID del producto
        deleteProduct(productId);
    }
});

function deleteProduct(productId) {
    // Hacer una solicitud fetch al servidor para eliminar un producto especificado por ID
    fetch(`${URL}/products/${productId}`, {
        method: 'DELETE',  // Especificar el método de solicitud como 'DELETE'
        headers: {
            // Incluir cualquier encabezado necesario, p.ej. para autenticación/autorización
        }
    })
        .then(response => {
            // Verificar si la respuesta es exitosa
            if (!response.ok) {
                // Si no es exitosa, lanza un error con el estado de la respuesta HTTP
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();  // O response.text() si no hay una respuesta JSON
        })
        .then(() => {
            // El producto se ha eliminado con éxito, actualizar la interfaz de usuario aquí
            console.log(`El producto con el ID ${productId} ha sido eliminado`);
            // Puedes elegir eliminar el elemento del DOM o refrescar la lista de productos
            // Aquí hay un ejemplo simple para eliminar la fila de la tabla del producto eliminado
            const productRow = document.querySelector(`button.delete-product[data-id="${productId}"]`).parentNode.parentNode;
            productRow.remove();
        })
        .catch(error => {
            // Captura y registro de cualquier error que ocurra durante la solicitud fetch
            console.error('Error al intentar eliminar el producto: ', error);
            alert('Error al intentar eliminar el producto.');
        });
}