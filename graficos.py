import pandas as pd
import plotly.express as px
import streamlit as st

def mostrar_analisis_radar(features_list):
    # 1. Convertimos a tabla y sacamos promedios
    df = pd.DataFrame(features_list)
    
    # Seleccionamos las métricas clave
    metricas = ['danceability', 'energy', 'valence', 'acousticness', 'instrumentalness']
    nombres_bonitos = ['Bailabilidad', 'Energía', 'Felicidad', 'Acústico', 'Instrumental']
    
    valores = df[metricas].mean().tolist()
    
    # 2. Creamos el DataFrame para el radar
    df_radar = pd.DataFrame({
        'Métrica': nombres_bonitos,
        'Valor': valores
    })

    # 3. Dibujamos el gráfico de Radar
    fig = px.line_polar(df_radar, r='Valor', theta='Métrica', line_close=True)
    
    # 4. Estilo "Spotify Dark"
    fig.update_traces(fill='toself', line_color='#1DB954')
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1], gridcolor="#444"),
            angularaxis=dict(gridcolor="#444")
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color="white",
        showlegend=False
    )
    
    st.write("### 🧊 Tu ADN Musical (Promedio)")
    st.plotly_chart(fig, use_container_width=True)