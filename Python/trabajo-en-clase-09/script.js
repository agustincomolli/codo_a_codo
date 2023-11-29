// Añadir producto
function addProduct(productData) {
    fetch('/products', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(productData),
    })
        .then(response => response.json())
        .then(data => {
            console.log('Producto añadido:', data);
            // Actualizar la vista de productos
            loadProducts();
        })
        .catch((error) => {
            console.error('Error al añadir producto:', error);
        });
}

// Cargar y mostrar la lista de productos
function loadProducts() {
    fetch('/products', {
        method: 'GET',
    })
        .then(response => response.json())
        .then(products => {
            const productsTable = document.getElementById('productsTable');
            // Limpiar tabla antes de cargar los nuevos productos
            productsTable.innerHTML = '';

            products.forEach(product => {
                const row = productsTable.insertRow();
                row.insertCell(0).textContent = product.name;
                row.insertCell(1).textContent = product.description;

                const editButton = document.createElement('button');
                editButton.textContent = 'Editar';
                editButton.onclick = () => loadProductForEdit(product.id);
                row.insertCell(2).appendChild(editButton);

                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Eliminar';
                deleteButton.onclick = () => deleteProduct(product.id);
                row.insertCell(3).appendChild(deleteButton);
            });
        })
        .catch((error) => {
            console.error('Error al cargar productos:', error);
        });
}

// Cargar producto para editar
function loadProductForEdit(productId) {
    fetch(`/products/${productId}`, {
        method: 'GET',
    })
        .then(response => response.json())
        .then(product => {
            document.getElementById('editName').value = product.name;
            document.getElementById('editDescription').value = product.description;
            document.getElementById('productId').value = product.id;
            // Aquí también cambiarías a la vista o modal del formulario de edición si fuera necesario
        })
        .catch(error => {
            console.error('Error al cargar el producto para editar:', error);
        });
}

// Actualizar producto
function updateProduct(productId, updatedData) {
    fetch(`/products/${productId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedData),
    })
        .then(response => response.json())
        .then(data => {
            console.log('Producto actualizado:', data);
            // Actualizar la vista de productos
            loadProducts();
        })
        .catch(error => {
            console.error('Error al actualizar el producto:', error);
        });
}

// Eliminar producto
function deleteProduct(productId) {
    if (confirm('¿Estás seguro de eliminar este producto?')) {
        fetch(`/products/${productId}`, {
            method: 'DELETE',
        })
            .then(() => {
                console.log('Producto eliminado');
                // Actualizar la vista de productos
                loadProducts();
            })
            .catch(error => {
                console.error('Error al eliminar el producto:', error);
            });
    }
}

// Evento de formulario para añadir producto
document.getElementById('addProductForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const description = document.getElementById('description').value;
    addProduct({ name, description });
    this.reset(); // Resetea el formulario después de enviar
});

// Evento de formulario para editar producto
document.getElementById('editProductForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const productId = document.getElementById('productId').value;
    const name = document.getElementById('editName').value;
    const description = document.getElementById('editDescription').value;
    updateProduct(productId, { name, description });
});

// Cargar productos cuando la DOM esté lista
document.addEventListener('DOMContentLoaded', loadProducts);