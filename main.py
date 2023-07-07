from fastapi import FastAPI
import pandas as pd
import numpy as np
import iso639
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

df_merged = pd.read_csv('movies_dataset_transformed.csv')

app=FastAPI()

@app.get('/peliculas_idioma/{idioma}')
def contar_peliculas_por_idioma(idioma: str):
    idioma_nombre = None
    resultado = {}

    try:
        idioma_codigo = iso639.to_iso639_1(idioma.lower())
        idioma_nombre = iso639.to_name(idioma_codigo)
    except ValueError:
        resultado["mensaje"] = f"No se encontró información para el idioma {idioma}"
        return resultado

    cantidad_peliculas = len(df_merged[df_merged['original_language'] == idioma_codigo])
    resultado["idioma"] = idioma_nombre
    resultado["cantidad_peliculas"] = cantidad_peliculas

    return resultado



@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula: str):
    resultado = {}

    pelicula_info = df_merged[df_merged['title'].str.lower() == pelicula.lower()]
    if not pelicula_info.empty:
        duracion = pelicula_info['runtime'].values[0]
        año = pelicula_info['release_year'].values[0]
        resultado["pelicula"] = pelicula
        resultado["duracion"] = duracion
        resultado["año"] = año
    else:
        resultado["mensaje"] = f"No se encontró información para la película {pelicula}"

    return resultado





@app.get('/franquicia/{franquicia}')
def franquicia(franquicia: str):
    resultado = {}

    franquicia_info = df_merged[df_merged['collection_unique'].str.lower() == franquicia.lower()]
    if not franquicia_info.empty:
        cantidad_peliculas = len(franquicia_info)
        ganancia_total = franquicia_info['revenue'].sum()
        ganancia_promedio = franquicia_info['revenue'].mean()
        resultado["franquicia"] = franquicia
        resultado["cantidad_peliculas"] = cantidad_peliculas
        resultado["ganancia_total"] = ganancia_total
        resultado["ganancia_promedio"] = ganancia_promedio
    else:
        resultado["mensaje"] = f"No se encontró información para la franquicia {franquicia}"

    return resultado



@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais: str):
    resultado = {}

    cantidad_peliculas = len(df_merged[df_merged['prod_countries'].str.contains(pais, case=False, na=False)])
    resultado["pais"] = pais
    resultado["cantidad_peliculas"] = cantidad_peliculas

    return resultado



@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora: str):
    resultado = {}

    productora_info = df_merged[df_merged['prod_companies_name'].str.contains(productora, case=False, na=False)]
    if not productora_info.empty:
        revenue_total = productora_info['revenue'].sum()
        cantidad_peliculas = len(productora_info)

        resultado["productora"] = productora
        resultado["revenue_total"] = revenue_total
        resultado["cantidad_peliculas"] = cantidad_peliculas
    else:
        resultado["productora"] = productora
        resultado["revenue_total"] = 0
        resultado["cantidad_peliculas"] = 0

    return resultado



@app.get('/get_director/{nombre_director}')
def get_director(nombre_director: str):
    resultado = {}

    director_info = df_merged[df_merged['director'].str.lower() == nombre_director.lower()]
    if not director_info.empty:
        director_success = director_info['return'].values[0]
        peliculas_info = director_info[['title', 'release_date', 'return', 'budget', 'revenue']].values.tolist()

        resultado["director_success"] = director_success
        resultado["peliculas_info"] = peliculas_info
    else:
        resultado["director_success"] = None
        resultado["peliculas_info"] = []

    return resultado



#Reemplazar nan de title ''
df_merged['title'].fillna('', inplace=True)

# Crear el vectorizador TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df_merged['title'])

# Crear el modelo de vecinos más cercanos
knn = NearestNeighbors(n_neighbors=10,metric='cosine', algorithm='brute')
knn.fit(tfidf_matrix)


@app.get('/recomendacion/{titulo}')
def recomendacion(titulo):
    # Obtener el índice de la película de referencia
    titulo = titulo.lower()
    indice_referencia = df_merged[df_merged['title'].str.lower() == titulo].index
    if len(indice_referencia) == 0:
        return {"error": f"No se encontró información para la película {titulo}"}
    
    # Calcular los k vecinos más cercanos a la película de referencia
    _, indices_similares = knn.kneighbors(tfidf_matrix[indice_referencia])
    
    # Obtener los nombres de las películas más similares
    peliculas_similares = df_merged.loc[indices_similares.flatten(), 'title']
    
    # Eliminar la película de referencia y las duplicadas
    peliculas_similares = peliculas_similares[peliculas_similares != titulo].unique()
    
    # Tomar solo las primeras 5 recomendaciones
    peliculas_recomendadas = peliculas_similares[:5]
    
    return {"recomendaciones": peliculas_recomendadas.tolist()}
