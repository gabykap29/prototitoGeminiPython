from fastapi import FastAPI
from pydantic import BaseModel
from controllers.consultas_controller import consultas
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

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
    print("datos: ", datos)
    return consultas(datos)

if __name__ == "__main__":
    # Aquí se especifica la dirección IP y el puerto en el que el servidor escuchará
    uvicorn.run(app, host="0.0.0.0", port=8000)
