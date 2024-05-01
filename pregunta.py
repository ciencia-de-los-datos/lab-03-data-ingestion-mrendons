"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

def ingest_data():
    with open('clusters_report.txt', 'r') as file:
        data = []
        next(file)  # Saltar la primera línea
        next(file)  # Saltar la segunda línea

        for line in file:
            columns = line.split() # Separar por espacios
            if len(columns) >= 1: # Si hay al menos un elemento
                try:
                    cluster = int(columns[0])   # Convertir a entero
                    cantidad_de_palabras_clave = int(columns[1]) # Convertir a entero
                    porcentaje_de_palabras_clave = float(columns[2].replace(',', '.')) # Convertir a float
                    principales_palabras_clave = ' '.join(columns[4:])  # Unir las palabras clave
                    data.append([cluster, cantidad_de_palabras_clave, porcentaje_de_palabras_clave, principales_palabras_clave]) # Agregar a la lista
                except ValueError:
                    # Si hay error al convertir a int o float, asumimos que es una línea adicional de palabras clave
                    if len(data) > 0:
                        principales_palabras_clave = ' '.join(columns) # Unir las palabras clave
                        data[-1][-1] += ' ' + principales_palabras_clave # Agregar a la última fila

    headers = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'] # Encabezados
    df = pd.DataFrame(data, columns=headers) # Crear DataFrame
    df.columns = df.columns.str.replace(' ', '_').str.lower()  # Reemplazar espacios por guiones bajos y convertir a minúsculas
    return df

# Test
print(ingest_data())
