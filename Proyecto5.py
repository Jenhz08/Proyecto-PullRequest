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

#Aporte Ariana
nuevos_datos={"Nombre": ["Orgullo y Prejuicio", "Notting Hill", "Kiki:entregas a domicilio"], 
"Género":["romance", "romance", "anime" ],
"Duración": ["2h07m", "2h04m", "1h42m"],
"Puntaje Rotten Tomatoes": [88, 85, 99]}

df_nuevos_datos = pd.DataFrame(nuevos_datos)

df = pd.concat([df, df_nuevos_datos], ignore_index=True)
print(df)