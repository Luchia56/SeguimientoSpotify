#Grafico no funciona porque el token no lo permite.

import streamlit as st
import requests
from graficos import mostrar_analisis_radar

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

st.title("🎧 Mis Estadísticas de Spotify")
st.write("Configura el periodo para ver tu propio Wrapped.")

# Tu TOKEN actual
TOKEN = "BQDmTnzZebFI7JgQT3S-5LHlFbONvR5w0oGGi0z5bkW3Kz5h_xyggtVxjGsBM0j1K9z4hNWIyFXUFA5nvNDZBwOH6imZFEum2A3tTRoLvbgB2bHy6CzwrZauysyjm1HElXtLHJvQa3C5M34nYZ5IFU3R0mbWB-_D3SLWknAmVJ1RR8t1hqtfbrX7zKdFwUf-AbSbT6Pa8_YD3LxFQ2146cRfWR1nJuZ51yKeMnPBbl5eSXQAjh27-ZuAqhASOf9pzqvJg_YOEjtNq3ryE8qfi4V4IjJ4ltTiRZmS3nfiFbkgJSSWvoxevmaLqFS8JSpHRjFeCSDxBWv9yBaBQRLh2qzawkincbNxjOIlToS-9XbIvV7nH1rW_7mzKi0rReYknw"

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
                
                col1, col2, col3 = st.columns([1, 3, 1])
                with col1: st.image(img, width=65)
                with col2:
                    st.markdown(f"**{i}. {nombre}**")
                    st.markdown(f"*{artista}*")
                with col3: st.link_button("Play", url_spotify)
            else:
                col1, col2 = st.columns([1, 4])
                with col1:
                    if item['images']: st.image(item['images'][0]['url'], width=65)
                with col2: st.markdown(f"### {i}. {nombre}")

        # --- FASE 3: ANÁLISIS DE AUDIO (Solo si eliges canciones) ---
        if tipo == "tracks":
            st.divider()
            # 1. Extraer los IDs
            ids = [t['id'] for t in datos['items']]
            ids_string = ",".join(ids)
            
            # 2. Consultar Audio Features
            url_feat = f"https://api.spotify.com/v1/audio-features?ids={ids_string}"
            res_feat = requests.get(url_feat, headers=headers)
            
            if res_feat.status_code == 200:
                features_list = res_feat.json()['audio_features']
                # 3. Llamar a la función del otro archivo
                mostrar_analisis_radar(features_list)
            else:
                st.warning("No se pudo cargar el análisis detallado. Revisa los permisos del token.")
    else:
        st.error("El token ha caducado. Por favor, genera uno nuevo en Spotify for Developers.")