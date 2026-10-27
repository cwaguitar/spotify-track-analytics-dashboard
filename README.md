# 🎵 Spotify Track Analytics: Análisis de Rendimiento y Atributos de Audio para Curaduría de Contenido

## 💼 Contexto del Negocio
En las plataformas de streaming de música, la retención de usuarios depende de la capacidad de ofrecer contenido que resuene con las tendencias de escucha. Sin embargo, los equipos de curaduría de contenido y marketing suelen tomar decisiones basadas en intuición más que en datos sobre qué canciones o artistas priorizar en las playlists oficiales.

El objetivo de este proyecto es analizar el catálogo de tracks de Spotify para identificar qué patrones de audio (tempo, energía, bailable, etc.) e indicadores de plataforma impactan directamente en la popularidad y alcance de una canción.

---

## 🎯 Problema a Resolver
1. **Falta de visibilidad sobre factores de éxito:** Dificultad para determinar qué atributos sonoros caracterizan a los temas con mayor rendimiento en la plataforma.
2. **Evaluación de alcance cruzado:** Necesidad de entender la relación entre la presencia de un track en playlists y listas de éxitos (*charts*) frente a su volumen total de reproducciones.

---

## 🛠️ Solución Implementada

Se construyó un flujo de análisis de datos de producto que procesa el catálogo de canciones, evalúa sus variables técnicas y expone los hallazgos en un dashboard interactivo en Power BI.

### 1. Procesamiento y Limpieza de Datos (Python / Pandas)
- Normalización de nombres de tracks y artistas para eliminar duplicados.
- Tratamiento de datos faltantes en métricas de audio y fechas de lanzamiento.
- Formateo de variables de interacción (presencia en playlists vs. reproductores de streaming).

### 2. Modelado y Métricas en Power BI
- Definición de KPIs para evaluar la distribución de canciones por nivel de popularidad.
- Segmentación por atributos de audio (*Danceability*, *Energy*, *Valence*, *BPM*).
- Análisis comparativo de rendimiento entre canciones en solitario vs. colaboraciones.

---

## 📊 Demostración Interactiva

![Spotify Dashboard](./images/spotify_demo.png)

---

## 🛠️ Stack Tecnológico
- **Python (Pandas):** Ingesta, limpieza y estructuración de los datos de Spotify.
- **Power BI Desktop:** Modelado de datos, creación de medidas DAX para agregaciones de popularidad y diseño de la interfaz interactiva.
- **Git & GitHub:** Control de versiones y documentación del caso de uso.

---

## 🚀 Cómo Ejecutar este Proyecto

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/cwaguitar/spotify-track-analytics-dashboard.git](https://github.com/cwaguitar/spotify-track-analytics-dashboard.git)
