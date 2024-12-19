# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv('data/netflix_data.csv')
# Filter the movies between 1990 and 1999 both inclusive from the raw data
netflix_1990s_df = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] <= 1999) & (netflix_df['type'] == 'Movie')]


plt.hist(netflix_1990s_df['duration'])
plt.xlabel('Duration')
plt.ylabel('Count')
plt.show()
duration = 110

# Filter action movies with duration < 90
neflix_1990s_short_action_df = netflix_1990s_df[(netflix_1990s_df['genre'] == 'Action') & (netflix_1990s_df['duration'] < 90)]

# Find count of action movies
short_movie_count = neflix_1990s_short_action_df.shape[0]
print(short_movie_count)
