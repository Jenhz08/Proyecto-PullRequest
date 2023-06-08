# Proyecto 5 Pull Request

##########################
#   Módulos 
##########################

import pandas as pd
import numpy as np 

#############################
#  Datos iniciales Jenny    #
#############################
 
data = {
    'Nombre de la película': ['El Padrino', 'Titanic', 'El Señor de los Anillos', 'Avatar', 'Harry Potter y la Piedra Filosofal'],
    'Productor': ['Francis Ford Coppola', 'James Cameron', 'Peter Jackson', 'James Cameron', 'David Heyman'],
    'Género': ['Drama', 'Romance', 'Fantasía', 'Ciencia ficción', 'Fantasía']
}

df = pd.DataFrame(data)
print(df)


#############################
#  Aporte  OCM 1            #
#############################

nuevas_observaciones = {
    'Nombre de la película': ['rapidos y furiosos'],
    'Productor': ['don Juan'],
    'Género': ['satira']
}

df_nuevas_observaciones = pd.DataFrame(nuevas_observaciones)

# Agregar las nuevas observaciones al DataFrame existente
df = df.append(df_nuevas_observaciones, ignore_index=True)

print(df)

#############################
#  Aporte  OCM 2            #
#############################

df_draft = nuevas_observaciones = {
    'Nombre de la película': ['Avatar 2: el camino del agua'],
    'Productor': ['James Cameron'],
    'Género': ['Ciencia Fic.']
}

df_OCM2 = pd.DataFrame(df_draft)

# Agregar las nuevas observaciones al DataFrame existente

df = df.append(df_OCM2, ignore_index=True)

print(df)