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
            columns = line.split()
            if len(columns) >= 1:
                try:
                    cluster = int(columns[0])
                    cantidad_de_palabras_clave = int(columns[1])
                    porcentaje_de_palabras_clave = float(columns[2].replace(',', '.'))
                    principales_palabras_clave = ' '.join(columns[4:])
                    data.append([cluster, cantidad_de_palabras_clave, porcentaje_de_palabras_clave, principales_palabras_clave])
                except ValueError:
                    # Si hay error al convertir a int o float, asumimos que es una línea adicional de palabras clave
                    if len(data) > 0:
                        palabras_clave = ' '.join(columns)
                        palabras_clave = palabras_clave.replace('.', '').replace(',', ',').strip()
                        data[-1][-1] += ' ' + palabras_clave

    headers = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    df = pd.DataFrame(data, columns=headers)
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace('.', '').str.replace(',', ',').str.strip()
    df.columns = df.columns.str.replace(' ', '_').str.lower()
    return df

# Test
print(ingest_data())




