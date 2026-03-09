# Data Quality - Feature Engineering and Selection

El presente proyecto busca encontrar, mediante la aplicación de buenas prácticas, cuáles son las features más relevantes para predecir el target, el cual es "User Rating", calificación  IMDb de usuarios en una escala en base 10.

Para ello se trabajó con un archivo que contiene datos relativos a series y pelícilas de anime.

Haciendo uso, de manera modular, de distintas funciones  es que se buscó en una primera instancia, realizar un análisis de calidad de datos, revisando aspectos básicos y seleccionando un primer conjunto de variables a eliminar. Para luego realizar un análisis exploratorio inicial considerando gráficos de distribuciones de las diferentes variables.

El siguiente paso fue realizar una transformación inicial de los datos, buscando unificar y llevar las distintas variables a un formato común y compatible que posibilite de mejor manera su posterior explorarción.

Luego se proseguió a una revisión de outliers.

Como última instancia se realizó una transformación final de variables, aplicando transformaciones como logaritmo o get_dummies y creación de aquellas features que se consideraron pertinentes.
 
Esta primera etapa del notebook finaliza con la creación de un pipeline que permite documentar y automatizar todas las distintas instancias de preprocesamiento de datos anteriormente descriptas, el cuál lee el dataset original y devuelve un dataset ya tratado.

Una vez que las variables existentes fueron procesadas y las necesarias creadas, se finaliza con la selección de features mediante la aplicación de tres diferentes métodos de selección, features que permitan predecir con la mayor precisión posible nuestro target.

Diccionario de datos:
- Title: Nombre de la animación
- Genre: Género(s) bajo el cual cae la animación, por ejemplo, Acción, Aventura, etc.
- User Rating: IMDb calificación de usuarios sobre 10.
- Number of Votes: Total de usuarios de IMDb que han calificado la animación.
- Runtime: Duración de la animación en minutos.
- Year: Año en que se estrenó o comenzó a emitirse la animación.
- Summary: Un resumen breve o completo de la trama de la animación. Resúmenes completos se obtienen cuando están disponibles.
- Stars: Lista de actores principales o actores de voz involucrados en la animación.
- Certificate: Certificación de la animación, por ejemplo, PG, PG-13, etc.
- Metascore: Calificación de Metascore, si disponible, que es una puntuación agregada de varios críticos.
- Gross: Ganancias brutas o recaudación en taquilla de la animación.
- Episode: Indicador binario si la lista es para un episodio de una serie (1 para sí, 0 para no).
- Episode Title: Título del episodio si la lista es para un episodio; de lo contrario, será None (Ninguno).

Dependencias:
- Numpy 
- Pandas 
- Matplotlib
- Seaborn
- sklearn.feature_selection.SequentialFeatureSelector
- sklearn.linear_model.LinearRegression
- sklearn.linear_model.LassoCV
