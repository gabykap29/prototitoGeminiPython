from fastapi import FastAPI
from pydantic import BaseModel
from controllers.consultas_controller import consultas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar el middleware CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
class DatosConsulta(BaseModel):
    consulta: str

@app.post("/consultas/")
async def procesar_consulta(datos: DatosConsulta):
    return consultas(datos)


