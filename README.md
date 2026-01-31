# 🎧 Mi Spotify Stats

¡Bienvenido a mi proyecto de estadísticas de Spotify! 
Esta es una aplicación web creada con **Streamlit** que se conecta a la API de Spotify para mostrar tus canciones y artistas más escuchados en diferentes periodos de tiempo.

## ✨ Características
* **Visualización de Top Tracks**: Listado de tus 10 canciones favoritas con portadas de álbumes.
* **Visualización de Top Artistas**: Tus artistas más escuchados con sus fotos de perfil.
* **Periodos Personalizables**: Elige entre el último mes, los últimos 6 meses o tu historial de varios años.
* **Integración con Spotify**: Botón directo de "Play" para escuchar cada canción en la plataforma oficial.
* **Diseño Dark Mode**: Interfaz personalizada con los colores corporativos de Spotify.

## 🛠️ Tecnologías utilizadas
* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/) (Frontend de la App)
* [Spotify Web API](https://developer.spotify.com/documentation/web-api) (Datos musicales)
* [Requests](https://requests.readthedocs.io/) (Peticiones HTTP)

## Fases
* Fase 1 (Completada ✅): Diseño visual, conexión manual con Token y lista de Tops.
* Fase 2 (Próxima 🔜): Conexión oficial (OAuth2) y automatización para que no caduque el token.
* Fase 3 (Creativa 🚀): Análisis de "Audio Features" (gráficos de energía/baile) y generador de Playlists.
* Fase 4 (Inteligencia Artificial 🧠): * Music Mood Analyzer: Integración con la API de OpenAI/Gemini para generar un perfil psicológico basado en tus gustos.

Smart Recommendations: Sistema de recomendación inteligente que predice tu próximo "vicio" musical mediante modelos de clasificación.

Generación de Prompts: Creación de descripciones creativas para tus nuevas listas de reproducción basadas en el análisis de letras y ritmos.

## 🚀 Cómo ejecutarlo localmente
1. Clona este repositorio.
2. Asegúrate de tener instalado Python.
3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt