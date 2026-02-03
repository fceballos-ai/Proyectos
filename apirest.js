import express from "express";
import dotenv from "dotenv";

dotenv.config();

const app = express();
app.use(express.json());

const PORT = process.env.PORT || 3000;

app.get("/", (req, res) => {
  res.json({ mensaje: "API Act 3 funcionando correctamente" });
});

app.get("/api/usuarios", (req, res) => {
  res.json([
    { id: 1, nombre: "Ana" },
    { id: 2, nombre: "Carlos" }
  ]);
});

app.listen(PORT, () => {
  console.log(`API escuchando en puerto ${PORT}`);
});
