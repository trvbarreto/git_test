const express = require('express');

const app = express();

// Retorna uma mensagem para quem requisitar a rota /
app.get('/', (request, response) => {
    response.send('Hello World!');
});

// Retorna um JSON para quem requisitar a rota /
app.get('/json', (request, response) => {
    return response.json({ message: 'Hello World!' });
});

// Chamada para startar a aplicação
app.listen(3333);