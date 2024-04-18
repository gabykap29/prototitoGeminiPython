from config.api_gemini import model
from config.api_gemini import genai

from pydantic import BaseModel

class DatosConsulta(BaseModel):
    consulta: str

def consultas(datos: DatosConsulta):
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
    consulta = datos.consulta
    try:
        
        response = model.generate_content(consulta)
        return response.text
    except Exception as e:
        return str("Error al realizar la consulta: " + str(e) + "\n")
