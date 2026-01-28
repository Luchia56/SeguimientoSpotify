import streamlit as st
import requests

# 1. Configuración de página
st.set_page_config(page_title="Mi Spotify Stats", page_icon="🎧")

# 2. Estilos CSS 
st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
    }
    h1 {
        color: #1DB954 !important;
        font-family: 'Helvetica', sans-serif;
    }
    h2, h3, .stMarkdown p {
        color: #FFFFFF !important;
    }
    .stSelectbox label p {
        color: #FFFFFF !important;
    }
    /* Estilo para los botones de Streamlit */
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
    div.stButton > button:hover, .stLinkButton a:hover {
        background-color: #1ed760 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎧 Mis Estadísticas de Spotify")
st.write("Configura el periodo para ver tu propio Wrapped.")

# Tu TOKEN actual (Cámbialo cuando caduque)
TOKEN = "BQBzSqsR6uhVmW2bsyYA-Vm5vyuyGmNNyTwrfc9PCZoBM6j7zKkcU3oKbwFXrpbRYSAlF58EecSN5LJSd7-V_Kdk8ZgeUL0n2mAcpdTQBo4rDKV77aTZoJZXWnDr6OK0rzTpCm7Vb_oJnX8T91jDrnbizdAcffk2egxTuqIlpn-rOXXO50kpwtxsM28lIwMsd-XEpGasMJake9d1d2zDd7AtbPEAisJQqeTt0VCemJPDIpa2BB5WxgpVfyWau6DhBWc1QoHJqurHiVN1-K_nftk30QTVGGE6AazuufyqCQimn5hx2-839xlSxc90NUE0HrOtsvmFYFGopy-WazcYW_8zUw4L_dpJkciH1zPuTr8b9eez9NdFd4K_ZK4bU05MEQ"

headers = {"Authorization": f"Bearer {TOKEN}"}

opcion = st.selectbox("¿Qué quieres ver?", ["Artistas favoritos", "Canciones top"])
tiempo_display = st.selectbox("¿De qué periodo?", ["Últimos 6 meses (Standard)", "Último mes (Reciente)", "Histórico (Varios años)"])

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
        
        for i, item in enumerate(datos['items'], 1):
            nombre = item['name']
            
            if tipo == "tracks":
                artista = item['artists'][0]['name']
                img = item['album']['images'][0]['url']
                url_spotify = item['external_urls']['spotify']
                
                col1, col2, col3 = st.columns([1, 3, 1])
                with col1:
                    st.image(img, width=65)
                with col2:
                    st.markdown(f"**{i}. {nombre}**")
                    st.markdown(f"*{artista}*")
                with col3:
                    st.link_button("Play", url_spotify)
            else:
                col1, col2 = st.columns([1, 4])
                with col1:
                    if item['images']:
                        st.image(item['images'][0]['url'], width=65)
                with col2:
                    st.markdown(f"### {i}. {nombre}")
    else:
        st.error("El token ha caducado. Por favor, genera uno nuevo en Spotify for Developers.")