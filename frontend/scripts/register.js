document.getElementById('registerForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('http://localhost:5000/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const result = await response.json();
        if (response.ok) {
            document.getElementById('registerResult').innerText = `Usuario registrado: ${result.user_id}`;
        } else {
            document.getElementById('registerResult').innerText = `Error: ${result.error}`;
        }
    } catch (error) {
        document.getElementById('registerResult').innerText = `Error de conexión: ${error}`;
    }
});

