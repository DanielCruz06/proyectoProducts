document.getElementById('productForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const price = document.getElementById('price').value;

    try {
        const response = await fetch('http://localhost:5001/products', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, price })
        });

        const result = await response.json();
        if (response.ok) {
            document.getElementById('productResult').innerText = `Producto creado con éxito. ID de producto: ${result.product_id}`;
        } else {
            document.getElementById('productResult').innerText = `Error: ${result.error}`;
        }
    } catch (error) {
        document.getElementById('productResult').innerText = `Error de conexión: ${error}`;
    }
});

document.getElementById('listProductsBtn').addEventListener('click', async () => {
    try {
        const response = await fetch('http://localhost:5001/products');
        const products = await response.json();

        const productList = document.getElementById('productList');
        productList.innerHTML = ''; // Limpiar la lista

        products.forEach(product => {
            const li = document.createElement('li');
            li.innerText = `ID: ${product.id}, Nombre: ${product.name}, Precio: ${product.price}`;
            productList.appendChild(li);
        });
    } catch (error) {
        document.getElementById('productList').innerText = `Error de conexión: ${error}`;
    }
});

