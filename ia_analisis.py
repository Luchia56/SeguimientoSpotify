import requests
import json
import os 
from dotenv import load_dotenv

#Cargar el archivo .env
load_dotenv()
api_key = os.getenv("GSK_API_KEY")

def generar_perfil_psicologico(lista_vibras):
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    vibras_texto = ", ".join(lista_vibras)
    
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {
                "role": "system",
                "content": "Eres un analista musical sarcástico. Analiza SOLO los artistas y canciones que te pase el usuario. NO te inventes otros nombres. Responde con un único párrafo de texto plano, sin listas, sin puntos, sin negritas. Todo texto seguido."
            },
            {
                "role": "user", 
                "content": f"Analiza mi personalidad según estas canciones: {vibras_texto}. No menciones a nadie más que a los de la lista."
            }
        ],
        "temperature": 0.6
    }
    if isinstance(lista_vibras, list):
        vibras_texto = ", ".join(lista_vibras)
    else:
        vibras_texto = lista_vibras
    print(f"DEBUG - Canciones enviadas: {vibras_texto}")
    try:
        response = requests.post(url, headers=headers, json=data)
        resultado = response.json()
        
        if 'choices' in resultado:
            return resultado['choices'][0]['message']['content']
        
        return f"Error real: {resultado.get('error', {}).get('message', 'Clave no activa')}"
            
    except Exception as e:
        return f"Error de conexión: {str(e)}"