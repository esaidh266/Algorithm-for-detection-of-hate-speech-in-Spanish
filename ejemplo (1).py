import joblib
import obtener_caracteristicas
import pandas as pd

# Cargar el modelo
modelo = joblib.load("nombre_del_modelo.joblib")

# Cargamos el archivo sobre el que realizar las predicciones
df = pd.read_csv("archivo_a_predecir.csv", delimiter=';')

# Dataframe en el que mostrar los resultados
resultados = pd.DataFrame()
resultados['CONTENIDO A ANALIZAR'] = df['CONTENIDO A ANALIZAR']

# Procesamos el dataframe
df = obtener_caracteristicas.main(df)

# Realizar la predicción
prediccion = modelo.predict(df)

# Añadimos las predcciones para visualizar los resultados
resultados['PREDICCIONES'] = prediccion
print(resultados)