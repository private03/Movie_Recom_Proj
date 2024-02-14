# src/recommendation_generator.py
def generate_recommendations_with_titles(user_id, ratings_data, movies_data, model, n_recommendations=10):
    all_movies = ratings_data['movieId'].unique()
    rated_movies = ratings_data[ratings_data['userId'] == user_id]['movieId'].unique()
    unrated_movies = [movie for movie in all_movies if movie not in rated_movies]
    
    predictions = [(movie, model.predict(user_id, movie).est) for movie in unrated_movies]
    predictions.sort(key=lambda x: x[1], reverse=True)
    
    top_recommendations = predictions[:n_recommendations]
    
    # Enhance recommendations with movie titles
    top_recommendations_with_titles = [(movie_id, movies_data.loc[movies_data['movieId'] == movie_id, 'title'].iloc[0], pred_rating) for movie_id, pred_rating in top_recommendations]
    
    return top_recommendations_with_titles
