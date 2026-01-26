import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import requests

# Pega aquí TODO el código que estaba entre las comillas después de Bearer
TOKEN = "BQCxPkoteeuEQDht7Ra6bVLaDeSmwIILvpfFPTNU2oHUgONiTAbs_1OQIdUk2XgMuoR9BmpdHOTQsaoZsPB3J421wlpSzejGB_38gRz--GDLNyCUKlRT1LlDy0zrvr-sKmVmReKPfzM8DmXa08Y8MMPQpS9afOqWZZg4Fx9bOVhnLT_Z6hzCsFufqixmoQXYDCOcy5kTX3eBEH4BcT2S7LhKLUV1TiY04tgzTXWv_Eer4oicKCSlHSxJPtkLa_-0M_nj6LvbHM64Wbz11vtKFd7gUk6CpRsYc2oIF5rZPpsSv8y1tSo0C4ZlDqwfujIXggZX9ZTbEcoEWiZTjyNDhNfCBPFjGp5EclSZBOwYa-m2jtPUAMEL1ZsS02zqu7GQ1A" 

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

# Consultamos tus artistas Top
url = "https://api.spotify.com/v1/me/top/artists?limit=10"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    datos = response.json()
    print("\n--- 🎧 MI WRAPPED PERSONAL: TOP ARTISTAS ---")
    for i, artista in enumerate(datos['items'], 1):
        print(f"{i}. {artista['name']}")
else:
    print(f"Error: {response.status_code}. Es posible que el token haya caducado.")

#Canciones más escuchadas
url = "https://api.spotify.com/v1/me/top/tracks"
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print("\n--- 🎵 MIS CANCIONES TOP ---")
    datos = response.json()
    for i, cancion in enumerate(datos['items'], 1):
        # cancion['name'] es el título
        # cancion['artists'][0]['name'] es el cantante principal
        print(f"{i}. {cancion['name']} - {cancion['artists'][0]['name']}")
else:
    print(f"Error: {response.status_code}")