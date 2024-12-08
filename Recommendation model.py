import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset of movies
data = {
    'MovieID': [1, 2, 3, 4, 5],
    'Title': ['The Matrix', 'Inception', 'Interstellar', 'The Godfather', 'Pulp Fiction'],
    'Genre': ['Sci-Fi Action', 'Sci-Fi Thriller', 'Sci-Fi Drama', 'Crime Drama', 'Crime Comedy'],
    'Description': [
        'A computer hacker learns about the true nature of his reality.',
        'A thief who steals secrets through dreams is given a tough mission.',
        'A team of explorers travel through a wormhole in space.',
        'The aging patriarch of an organized crime dynasty transfers control.',
        'The lives of two hitmen intertwine with unexpected events.'
    ],
}

# Load the dataset into a DataFrame
movies_df = pd.DataFrame(data)

# Step 1: Combine Genre and Description for feature extraction
movies_df['Features'] = movies_df['Genre'] + " " + movies_df['Description']

# Step 2: TF-IDF Vectorization on combined features
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['Features'])

# Step 3: Compute cosine similarity for all movies
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Step 4: Recommendation function
def recommend_movies(movie_title, movies_df, cosine_sim, top_n=3):
    try:
        # Find the index of the movie in the dataset
        idx = movies_df[movies_df['Title'] == movie_title].index[0]
    except IndexError:
        return ["Movie not found in the dataset."]
    
    # Get pairwise similarity scores for the movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort by similarity scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get indices of the top N similar movies (excluding itself)
    sim_scores = sim_scores[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]
    
    # Return the top recommended movie titles
    return movies_df.iloc[movie_indices]['Title'].tolist()

# Step 5: Test the recommendation system
user_input = "Inception"
recommended_movies = recommend_movies(user_input, movies_df, cosine_sim, top_n=3)
print(f"Because you liked '{user_input}', we recommend: {', '.join(recommended_movies)}")
