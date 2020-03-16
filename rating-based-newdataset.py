# -*- coding: utf-8 -*-
import pandas as pd
import operator as op
# Get the data 
column_names=['movie_title','imdb_score']
path = 'movie_metadata.csv'
df = pd.read_csv(path)
movie= df[column_names].copy()

#add column index
count_row = movie.shape[0] 
cc= [x for x in range(count_row)]
movie['index']=cc

#handle missing values
column_names= list(movie)
for c in column_names:
  movie[c]=movie[c].fillna('')
print(movie.iloc[0][1])   

#computing distance between two movies
def ComputeDistance(a, b):
    knndist = abs(a-b)
    return  knndist    
    
#fetching k neighbours
def getNeighbors(movieID, K):
    distances = []
    for id in range(count_row):
        if (id != movieID):
            dist = ComputeDistance(movie.iloc[movieID][1], movie.iloc[id][1])
            distances.append((id, dist))
    distances.sort(key=lambda elem: elem[1])
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])
    return neighbors

K = 10
neighbors = getNeighbors(3, K) 
print (movie.iloc[3][0] + str(movie.iloc[3][1]))
for neighbor in neighbors:
    print (movie.iloc[neighbor][0] + str(movie.iloc[neighbor][1]))
  
