import plotly.graph_objects as go
import streamlit as st

def generar_radar_vibes(lista_de_vibras):
    """
    Traduce las etiquetas de texto a valores numéricos para el radar.
    """
    # 1. Definimos los ejes del radar
    categorias = ['Energía', 'Bailabilidad', 'Felicidad (Valencia)', 'Acústica', 'Ritmo Latino']
    
    # 2. Diccionario de pesos (Cómo puntúa cada etiqueta)
    puntuaciones = {
        'rock': [0.9, 0.4, 0.5, 0.2, 0.1],
        'pop': [0.7, 0.7, 0.8, 0.4, 0.3],
        'reggaeton': [0.8, 0.9, 0.7, 0.1, 0.9],
        'latin': [0.7, 0.8, 0.8, 0.3, 0.9],
        'dance': [0.9, 0.9, 0.7, 0.1, 0.4],
        'rnb': [0.5, 0.6, 0.5, 0.6, 0.3],
        'hip-hop': [0.8, 0.7, 0.5, 0.2, 0.3],
        'funk': [0.8, 0.9, 0.8, 0.2, 0.5],
        'trap': [0.8, 0.7, 0.4, 0.1, 0.6],
        'bachata': [0.6, 0.8, 0.7, 0.4, 1.0],
        'flamenco urbano': [0.7, 0.7, 0.6, 0.5, 0.9],
        'folk': [0.4, 0.3, 0.5, 0.8, 0.2]
    }

    # Valores iniciales (promedio)
    valores = [0.1] * 5
    conteo = 0

    # 3. Procesamos las vibras recolectadas
    for vibe in lista_de_vibras:
        vibe = vibe.lower()
        if vibe in puntuaciones:
            for i in range(5):
                valores[i] += puntuaciones[vibe][i]
            conteo += 1

    # Normalizamos los valores (hacemos el promedio)
    if conteo > 0:
        valores = [v / conteo for v in valores]
    else:
        # Valores por defecto si no hay coincidencias
        valores = [0.5, 0.5, 0.5, 0.5, 0.5]

    # 4. Crear el gráfico con Plotly
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=valores,
        theta=categorias,
        fill='toself',
        name='Tu ADN Musical',
        line_color='#1DB954', # Verde Spotify
        fillcolor='rgba(29, 185, 84, 0.3)'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1])
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white", size=14)
    )

    return fig