import streamlit as st
import requests
from graficos import generar_radar_vibes
import os 
from dotenv import load_dotenv
from ia_analisis import generar_perfil_psicologico



#Carga de configuracion y llaves. 
load_dotenv() # Carga el archivo .env

api_key = os.getenv("LASTFM_API_KEY")
api_secret = os.getenv("LASTFM_SHARED_SECRET")

if api_key:
    print(f"Llave de Last.fm cargada correctamente: {api_key[:5]}...")

def obtener_vibras_cancion(artista, cancion):
    # 1. Lista de etiquetas que NO queremos (porque confunden al radar)
    lista_negra = [
        "eurovision", "ukrainian", "bielorrusia", "belarus", 
        "spotify", "all", "unknown vibe", "musical energy",
        "female vocalists", "seen live"
    ]
    
    nombre_limpio = cancion.split('(')[0].strip()
    url = "http://ws.audioscrobbler.com/2.0/"
    
    try:
        #Lógica de búsqueda 
        res = requests.get(url, params={"method": "track.gettoptags", "artist": artista, "track": nombre_limpio, "api_key": api_key, "format": "json"})
        tags = [t['name'].lower() for t in res.json().get('toptags', {}).get('tag', [])]
        
        if not tags:
            res_art = requests.get(url, params={"method": "artist.gettoptags", "artist": artista, "api_key": api_key, "format": "json"})
            tags = [t['name'].lower() for t in res_art.json().get('toptags', {}).get('tag', [])]

        # 2. APLICAMOS EL FILTRO: Solo dejamos las que NO están en la lista negra
        tags_filtrados = [t for t in tags if t not in lista_negra][:5]
        
        # 3. PLAN C: Si después de filtrar se queda vacío, ponemos algo genérico
        if not tags_filtrados:
            return ["pop", "latin"]
            
        return tags_filtrados
        
    except:
        return ["pop"]

# 1. Configuración de página
st.set_page_config(page_title="Mi Spotify Stats", page_icon="🎧")

# 2. Estilos CSS 
st.markdown("""
    <style>
    .stApp { background-color: #121212; }
    h1 { color: #1DB954 !important; font-family: 'Helvetica', sans-serif; }
    h2, h3, .stMarkdown p { color: #FFFFFF !important; }
    .stSelectbox label p { color: #FFFFFF !important; }
    div.stButton > button, div.stDownloadButton > button, .stLinkButton a {
        background-color: #1DB954 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 8px 20px !important;
        font-weight: bold !important;
        text-decoration: none !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    div.stButton > button:hover, .stLinkButton a:hover { background-color: #1ed760 !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Forzamos TODO el texto dentro de la caja a ser blanco puro */
    .veredicto-final, .veredicto-final p, .veredicto-final li, .veredicto-final span, .veredicto-final div {
        color: #FFFFFF !important;
        background-color: transparent !important;
    }
    .veredicto-box-container {
        background-color: #282828 !important;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #1DB954;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎧 Mis Estadísticas de Spotify")
st.write("Configura el periodo para ver tu propio Wrapped.")

# Tu TOKEN actual
TOKEN = "BQAdFdaBUJa_SXH4kKNHo1t-eyOAxxZXOm9zvhJp1R14TFrtc-XQwaT3658pMu1IHAMpgEuwvY-UDAhYkUTCk2ynvXkSOmz-ogE1-9aav4IebV8N6NNU2INF5YdZ75ojukyWerWQtuvmJ0isPDqyB5g8lfzHC3gbq2KVetKHSqajzvrnyUeMdB9Eyd3brb4-8ytQBvkhrINlqi1UZZ9-gv1bZzG1H4QWvXOfNzM8VByHYPScGarJHX08pGYYa6zv3lZO7YNNdVJgIBu9T3rU4imdGsS9J602Yu3TLLEA1SKJFQ"

headers = {"Authorization": f"Bearer {TOKEN}"}

opcion = st.selectbox("¿Qué quieres ver?", ["Artistas favoritos", "Canciones top"])
tiempo_display = st.selectbox("¿De qué periodo?", ["Último mes (Reciente)", "Últimos 6 meses (Standard)", "Histórico (Varios años)"])

mapping = {
    "Último mes (Reciente)": "short_term",
    "Últimos 6 meses (Standard)": "medium_term",
    "Histórico (Varios años)": "long_term"
}
time_range = mapping[tiempo_display]

if st.button("Actualizar datos"):
    tipo = "artists" if opcion == "Artistas favoritos" else "tracks"
    url = f"https://api.spotify.com/v1/me/top/{tipo}?time_range={time_range}&limit=10"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        datos = response.json()
        st.subheader(f"Tu Top de {opcion}")
        
        # Mostramos la lista de canciones o artistas
        for i, item in enumerate(datos['items'], 1):
            nombre = item['name']
            
            if tipo == "tracks":
                artista = item['artists'][0]['name']
                img = item['album']['images'][0]['url']
                url_spotify = item['external_urls']['spotify']
                
                # --- NUEVA LÓGICA: Obtener Tags de Last.fm ---
                vibras = obtener_vibras_cancion(artista, nombre)
                
                col1, col2, col3 = st.columns([1, 3, 1])
                with col1: 
                    st.image(img, width=65)
                with col2:
                    st.markdown(f"**{i}. {nombre}**")
                    st.markdown(f"*{artista}*")
                    # Mostramos las etiquetas si existen
                    if vibras:
                        st.caption(f"✨ Vibes: {', '.join(vibras)}")
                with col3: 
                    st.link_button("Play", url_spotify)
            else:
                col1, col2 = st.columns([1, 4])
                with col1:
                    if item['images']: 
                        st.image(item['images'][0]['url'], width=65)
                with col2: 
                    st.markdown(f"### {i}. {nombre}")

       # --- FASE 3: RECOLECCIÓN DE DATOS (Canciones + Vibras) ---
        st.divider()
        st.subheader("📊 Tu Análisis de Estilo")
        
        todas_las_vibras = []
        lista_canciones_para_ia = [] # Nueva lista para guardar "Canción - Artista"

        for item in datos["items"]:
            # 1. Adaptamos la extracción según si es artista o canción
            if tipo == "tracks":
                nombre = item["name"]
                artista = item["artists"][0]["name"]
                lista_canciones_para_ia.append(f"{nombre} de {artista}")
                # Para las canciones buscamos las vibras de la canción
                vibras = obtener_vibras_cancion(artista, nombre)
            else:
                # Si es un artista, el nombre ya es el artista directamente
                artista = item["name"]
                lista_canciones_para_ia.append(f"Artista: {artista}")
                # Para artistas podemos pedir directamente los tags de Last.fm usando solo el nombre del artista
                vibras = obtener_vibras_cancion(artista, "")

            todas_las_vibras.extend(vibras)
        
        # Generamos y mostramos el radar (usa etiquetas)
        if todas_las_vibras:
            figura = generar_radar_vibes(todas_las_vibras)
            st.plotly_chart(figura, use_container_width=True)
            st.info("💡 Este radar analiza los ritmos y géneros detectados en Last.fm.")
        
        # --- FASE 4: EL VEREDICTO FINAL ---
        st.divider()
        st.subheader("🤖 El Veredicto de tu ADN Musical")
        
        if tipo == "tracks":
            lista_nombres_limpios = [
                f"{item['name']} de {item['artists'][0]['name']}"
                for item in datos["items"]
            ]
        else:
            lista_nombres_limpios = [item["name"] for item in datos["items"]]

        texto_para_ia = ". ".join(lista_nombres_limpios)
        
        with st.spinner("Limpiando los datos y analizando..."):
            perfil = generar_perfil_psicologico(texto_para_ia)
            
            # Usamos una sola clase limpia para que el CSS de arriba funcione
            st.markdown(f'<div class="veredicto-box">{perfil}</div>', unsafe_allow_html=True)
    else:
        st.error("El token ha caducado. Por favor, genera uno nuevo en Spotify for Developers.")