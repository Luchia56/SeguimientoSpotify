# 🎧 Music Mind: Spotify Stats & AI Mood Analyzer

¡Bienvenido a mi proyecto de análisis musical! Esta aplicación web, construida con **Streamlit**, permite a los usuarios explorar sus hábitos de escucha y entender la "psicología" detrás de sus canciones favoritas. 

Debido a las restricciones de acceso de la API de Spotify para desarrolladores (febrero 2026), este proyecto utiliza una **arquitectura híbrida** que combina datos de Spotify con la flexibilidad de la API de Last.fm para ofrecer un análisis profundo sin coste alguno.

## ✨ Características Principales

* **Visualización de Tops:** Listado de tus 10 canciones y artistas más escuchados.
* **Análisis de "Vibes" (Estado de Ánimo):** Integración con **Last.fm API** para obtener etiquetas (tags) emocionales de cada pista.
* **Diseño Dark Mode:** Interfaz personalizada con los colores corporativos de Spotify para una experiencia inmersiva.
* **Periodos Personalizables:** Elige entre el último mes, los últimos 6 meses o tu historial de varios años.
* **IA Mood Analyzer (Fase 4):** Generación de un perfil psicológico del usuario basado en el análisis de sentimientos de las letras y ritmos detectados.

## 🛠️ Stack Tecnológico

* **Frontend:** [Streamlit](https://streamlit.io/) (Python).
* **APIs de Datos:** * **Spotify Web API:** Estructura de visualización y metadatos básicos.
    * **Last.fm API:** Fuente principal para análisis de géneros y sentimientos (Gratuita).
* **Procesamiento:** Python (Requests, Pandas).
* **IA:** Integración con modelos de lenguaje para el análisis de perfil de usuario.

## 🚀 Adaptabilidad y Resiliencia Técnica

Este proyecto es un ejemplo de **adaptación ante cambios de infraestructura**. Tras la decisión de Spotify de limitar la creación de nuevas aplicaciones a cuentas Premium y restringir los *Audio Features*, el sistema fue rediseñado para:
1.  Utilizar **Last.fm** como motor de etiquetas (tags) gratuito.
2.  Mantener la interfaz de usuario de Spotify pero con datos enriquecidos externamente.
3.  Garantizar que la aplicación sea accesible para todos los usuarios, independientemente de su tipo de suscripción.

## ⚙️ Instalación y Uso Local

1.  Clona el repositorio.
2.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3.  Crea un archivo `.env` o configura tus `secrets` en Streamlit con:
    * `LASTFM_API_KEY`: Tu clave de la API de Last.fm.
    * `LASTFM_SHARED_SECRET`: Tu secreto de Last.fm.
    * `SPOTIPY_CLIENT_ID`: (Opcional si usas el modo demo).

4.  Ejecuta la app:
    ```bash
    streamlit run app.py
    ```

## 📈 Roadmap

* **Fase 1:** Diseño visual y conexión manual. ✅
* **Fase 2:** Integración con Last.fm para evitar muros de pago de Spotify. 🔜
* **Fase 3:** Visualización avanzada de "Vibes" mediante gráficos de radar. 🔜
* **Fase 4:** Music Mood Analyzer e Inteligencia Artificial aplicada. 🚀