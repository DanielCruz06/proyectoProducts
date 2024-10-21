document.getElementById('loginForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('http://localhost:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const result = await response.json();
        if (response.ok) {
            document.getElementById('loginResult').innerText = `Sesión iniciada con éxito. ID de usuario: ${result.user_id}`;
        } else {
            document.getElementById('loginResult').innerText = `Error: ${result.error}`;
        }
    } catch (error) {
        document.getElementById('loginResult').innerText = `Error de conexión: ${error}`;
    }
});

