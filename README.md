# Proyecto Individual 1: ML Ops
Este proyecto es parte de la Carrera de Data Science en SoyHenry, DT12/2023.



## Objetivo
El objetivo del proyecto es simular el trabajo de un Data Scientist en una start-up que provee servicios de agregación de plataformas de streaming, y lograr un MVP (Minimum Viable Product).  
En este proyecto creo mi primer modelo de ML que soluciona un problema de negocio: un sistema de recomendación de peliculas por similitud.

### Flujo de trabajo
![Flujo ML](https://github.com/MaryFlorence/test1/blob/master/flujo%20ML%20Ops.png)



### Metodos utilizados
* ETL
* EDA
* Machine Learning
* Data Visualization
* API


### Librerias y Tecnologias utilizadas
* Python
* Pandas, numpy
* Matplotlib, Scikit-learn
* seaborn, ast, re, iso639
* FastAPI
* Render
* Uvicorn

## Proceso de ETL y EDA

En este repositorio se encuentran los notebooks de ETL y EDA para mayor detalle. En la etapa de ETL, luego de la extracción, se realizan operaciones para limpiar y preparar los datos.  Principalmente, se realizaron acciones como el desanidamiento de columnas, la conversión de formatos de datos, la generación de nuevas columnas,la eliminación de columnas innecesarias, y eliminación de valores nulos. Para el proceso de EDA, se analiza la estructura y tamaño del dataset. Se hace un analisis estadistico, descriptivo, y de correlaciones. Se devuelven conclusiones para el equipo de Marketing.

## Exploremos la API 
Render: https://test1deploy.onrender.com/docs#/

La API proporciona diversas funciones y características basadas en el análisis de datos y técnicas de Machine Learning para interactuar con el conjunto de datos de películas. A continuación, se describen las principales funciones disponibles:

1. peliculas_idioma(Idioma: str)
Esta función recibe como entrada un idioma y devuelve la cantidad de películas producidas en ese idioma. El resultado se presenta en formato de texto indicando la cantidad de películas estrenadas en el idioma especificado.

Ejemplo de retorno: "Se estrenaron X películas en idioma".

2. peliculas_duracion(Pelicula: str)
Mediante esta función, se puede obtener información sobre una película específica. Se ingresa el nombre de la película y la función devuelve la duración y el año de lanzamiento de la misma. El resultado se presenta en formato de texto indicando la duración y el año correspondientes.

Ejemplo de retorno: "Duración: X minutos. Año: XXXX".

3. franquicia(Franquicia: str)
Al proporcionar el nombre de una franquicia, esta función devuelve información sobre la cantidad de películas pertenecientes a dicha franquicia, así como la ganancia total y el promedio de ganancias de todas las películas de la franquicia. El resultado se presenta en formato de texto indicando la cantidad de películas, la ganancia total y la ganancia promedio.Recomendacion: ingresar el nombre de la pelicula + 'collection'.

Ejemplo de retorno: "La franquicia X tiene un total de X películas, con una ganancia total de X y una ganancia promedio de X".

4. peliculas_pais(Pais: str)
Esta función permite conocer la cantidad de películas producidas en un país determinado. Se ingresa el nombre del país y la función devuelve la cantidad de películas producidas en ese país. El resultado se presenta en formato de texto indicando la cantidad de películas producidas en el país especificado.

Ejemplo de retorno: "Se produjeron X películas en el país X".

5. productoras_exitosas(Productora: str)
Mediante esta función, se puede obtener información sobre una productora en particular. Se ingresa el nombre de la productora y la función devuelve el revenue total generado por las películas de la productora y la cantidad de películas realizadas por la misma. El resultado se presenta en formato de texto indicando el revenue total y la cantidad de películas.

Ejemplo de retorno: "La productora X ha obtenido un revenue total de X a través de X películas".

6. get_director(nombre_director)
Esta función recibe como entrada el nombre de un director y devuelve información sobre el éxito del director basado en el retorno de las películas. Además, devuelve una lista con el nombre de cada película dirigida por el director, junto con la fecha de lanzamiento, el retorno individual, el costo y la ganancia de cada película.

Ejemplo de retorno: "El director X ha tenido un éxito medido a través del retorno. Las películas dirigidas por el director son: [Película 1: Fecha de lanzamiento: X, Retorno: X, Costo: X, Ganancia: X], [Película 2: Fecha de lanzamiento: X, Retorno: X, Costo: X, Ganancia: X], ..."

7. recomendacion(titulo)
Esta función utiliza algoritmos de Machine Learning para recomendar películas similares basándose en una película de referencia. Se ingresa el nombre de una película y la función devuelve una lista con las 5 películas más similares.

Ejemplo de retorno: ["Película 1", "Película 2", "Película 3", "Película 4", "Película 5"]

Esta función utiliza técnicas de procesamiento de lenguaje natural y algoritmos de vecinos más cercanos (k-nearest neighbors) para encontrar las películas más similares a la película de referencia. Se utiliza el modelo TF-IDF (Term Frequency-Inverse Document Frequency) para representar las películas en forma de vectores y se calcula la similitud de coseno entre ellos.

Es importante destacar que esta función depende de un conjunto de datos previamente procesado y un modelo entrenado con películas disponibles. Si el nombre de la película de referencia no se encuentra en el conjunto de datos o no hay suficientes películas similares, se devolverá un mensaje de error indicando que no se encontró información para la película especificada.

## Contact
* Linkedin:https://www.linkedin.com/in/mariaflorencialuppi/
