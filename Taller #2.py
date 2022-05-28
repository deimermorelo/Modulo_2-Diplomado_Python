# Solucion al Taller 2
# Diplomado Python Aplicado a la Ingenieria UPB
# Autor: Deimer David Morelo Ospino
# ID: 502217
# Email: deimer.morelo@upb.edu.co

import pandas as pd
import numpy as np
import random 

#Punto 1
my_data = pd.read_csv('netflix_titles.csv')

#Punto 2
print(my_data.head(5))
print(my_data.tail(5))

#Punto 3
print(my_data.dtypes)

#Punto 4
my_data.to_excel("Netflix_list.xlsx", sheet_name="títulos", index=False)

#Punto 5
new_my_data = my_data.loc[:,['type','duration','description','country']]

#Punto 6
my_data["duracion"] = pd.to_numeric(my_data['duration'].replace('([^0-9]*)','', regex=True), errors='coerce')
movies_100 = my_data[my_data['type'].str.contains('Movie', na=False)]
movies_100_min = movies_100[movies_100['duracion']>100]

#Punto 7
tv_show = my_data[my_data['type'].str.contains('TV Show', na=False)]
tv_show_3_seasons= tv_show[tv_show['duracion']>3]

#Punto 8
categorias = my_data.loc[my_data['listed_in'].isin(['Documentaries','International TV Shows, TV Dramas, TV Mysteries'])]

# Punto 9. Recuerde usar casos con indexación numérica y con texto (loc / iloc).

#Punto 10
my_data.iloc[:5,0]='s1'
tv_show.loc[3450:,'listed_in']='Comedies, Horror Movies'

#Punto 11
my_data["Visto"] = np.random.randint(0, 2, my_data.shape[0])

