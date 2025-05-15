# importar la libreria pandas que es fundamental para el analisis de datos
import pandas as pd

# define la ruta del archivo csv que contiene los datos
# Si el archivo esta en el mismo directorio que el script basta con poner el nombre del archivo
# Si el archivo esta en otra carpeta se debe poner la ruta completa
path = 'Online_Retail.csv'

# lee el archivo csv  usando la funcion read_csv de pandas
# Se especifica la codificacion latin 1 para que se puedan leer los caracteres especiales
retail_data = pd.read_csv(path, encoding='latin1')

# Muestra el tipo de la variable retail_data para confirmar que es un dataframe
# Un dataframe es una estructura de datos bidimensional similar a una tabla
print(type(retail_data))

# imprime todo el contenido del dataframe
print(retail_data)
