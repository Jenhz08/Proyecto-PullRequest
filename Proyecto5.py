# Proyecto 5 Pull Request

import pandas as pd

data = {
    'Nombre de la película': ['El Padrino', 'Titanic', 'El Señor de los Anillos', 'Avatar', 'Harry Potter y la Piedra Filosofal'],
    'Productor': ['Francis Ford Coppola', 'James Cameron', 'Peter Jackson', 'James Cameron', 'David Heyman'],
    'Género': ['Drama', 'Romance', 'Fantasía', 'Ciencia ficción', 'Fantasía']
}

df = pd.DataFrame(data)
print(df)