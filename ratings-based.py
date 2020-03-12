
import pandas as pd 
  
# Get the data 
column_names = ['user_id', 'item_id', 'rating', 'timestamp'] 
path = 'file.tsv'
df = pd.read_csv(path, sep='\t', names=column_names) 
  
# Check the head of the data 
df.head(10) 
movie_titles = pd.read_csv('Movie_Id_Titles.csv') 
movie_titles.head() 

#merging dataframes
data = pd.merge(df, movie_titles, on='item_id') 
data.head()

# creating dataframe with 'rating' count values 
ratings = pd.DataFrame(data.groupby('title')['rating'].mean())  
ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count()) 
ratings.head() 

# Sorting values according to  
# the 'num of rating column' 
moviemat = data.pivot_table(index ='user_id', columns ='title', values ='rating') 
moviemat.head() 
ratings.sort_values('num of ratings', ascending = False).head(10)

# analysing correlation with similar movies 
starwars_user_ratings = moviemat['Star Wars (1977)'] 
liarliar_user_ratings = moviemat['Liar Liar (1997)'] 
starwars_user_ratings.head(30)

# analysing correlation with similar movies 
similar_to_starwars = moviemat.corrwith(starwars_user_ratings) 
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings) 
corr_starwars = pd.DataFrame(similar_to_starwars, columns =['Correlation']) 
corr_starwars.dropna(inplace = True) 
corr_starwars.head()

# Similar movies like starwars 
corr_starwars.sort_values('Correlation', ascending = False).head(10) 
corr_starwars = corr_starwars.join(ratings['num of ratings']) 
corr_starwars.head() 
corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending = False).head() 

