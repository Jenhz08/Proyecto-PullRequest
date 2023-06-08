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

##Marco 
pelicula={"Nombre": ["Super Mario Bros", "The Whale", "Spiderman: Across", "Notting Hill", "Kiki:entregas a domicilio", "Green Book"], 
"Género":["animada", "drama", "animada", "romance", "anime", "Drama" ],
"Duración": ["1h32m", "1h57m", "2h20m", "2h04m", "1h42m", "2h10m"],
"Puntaje Rotten Tomatoes": [60, 65, 96, 85, 99, 77]}
pl= pd.DataFrame(pelicula)
print(pl)
