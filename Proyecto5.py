# Proyecto 5 Pull Request

import pandas as pd

data = {
    'Nombre de la película': ['El Padrino', 'Titanic', 'El Señor de los Anillos', 'Avatar', 'Harry Potter y la Piedra Filosofal'],
    'Productor': ['Francis Ford Coppola', 'James Cameron', 'Peter Jackson', 'James Cameron', 'David Heyman'],
    'Género': ['Drama', 'Romance', 'Fantasía', 'Ciencia ficción', 'Fantasía']
}

df = pd.DataFrame(data)
print(df)


#Aporte OCM
nuevas_observaciones = {
    'Nombre de la película': ['rapidos y furiosos'],
    'Productor': ['don Juan'],
    'Género': ['satira']
}

df_nuevas_observaciones = pd.DataFrame(nuevas_observaciones)

# Agregar las nuevas observaciones al DataFrame existente
df = df.append(df_nuevas_observaciones, ignore_index=True)

print(df)

#############
### Marco ###
#############
nuevos_datos = {
    'Nombre de la película': ['Green Book', 'the shawshank redemption ', 'notting hill'],
    'Productor': ['Peter Farrelly', 'Niki Marvin', 'Duncan Kenworthy'],
    'Género': ['Drama', 'drama', 'romantica']
    }
act=pd.concat([df,pd.DataFrame(nuevos_datos)],ignore_index=True)
print(act)
