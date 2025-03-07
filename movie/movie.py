import pandas as pd

column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('file.tsv', sep='\t', names=column_names)  # Yerel dosyayı oku

print(df.head())

movie_titles = pd.read_csv("Movie_Id_Titles.csv")
movie_titles.head()

data = pd.merge(df, movie_titles, on='item_id')
data.head()

#Calculate mean rating of all movies
data.groupby('title')['rating'].mean().sort_values(ascending=False)

# creating dataframe with 'rating' count values
ratings = pd.DataFrame(data.groupby('title')['rating'].mean())

ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())
ratings.head()

#%% Visualization

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('white')


# plot graph of 'num of ratings column'
plt.figure(figsize=(10,4))
ratings['num of ratings'].hist(bins=70)
plt.show()

# plot graph of 'ratings' column
plt.figure(figsize=(10,4))
ratings['rating'].hist(bins = 70)
plt.show()
#%%

# Sorting values according to 
# the 'num of rating column'

moviemat = data.pivot_table(index = 'user_id',
                            columns = 'title',
                            values = 'rating')
moviemat.head()

ratings.sort_values('num of ratings', ascending=False).head(10)


# analysing correlation with similar movies
starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']

starwars_user_ratings.head()

similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.head()

# Similar movies like starwars
corr_starwars.sort_values('Correlation', ascending=False).head(10)
corr_starwars = corr_starwars.join(ratings['num of ratings'])

corr_starwars.head()

corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending=False).head()

# Similar movies like liarliar
corr_liarliar = pd.DataFrame(similar_to_liarliar, columns=['Correlation'])
corr_liarliar.dropna(inplace=True)

corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation', ascending = False).head()







