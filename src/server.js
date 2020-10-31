const express = require("express");
const cors = require("cors");

const api = require("./services/api");

const app = express();

app.use(cors());
app.use(express.json());

app.get('/', async (request, response) => {

  const { data } = await api.get("/");

  return response.json(data);
});

app.post('/test', async (request, response) => {
  const body = request.body;  

  const { data } = await api.post('/test', body);

  return response.json(data);
});

app.listen(3333, () => {
  console.log('🚀 Server started!');
});
