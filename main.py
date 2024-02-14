# main.py
from src.collaborative_filtering import CollaborativeFiltering
from src.data_processing import get_data
# Ensure you're importing the correctly updated recommendation generator function
from src.recommendation_generator import generate_recommendations_with_titles

def main():
    # Load and preprocess data
    ratings_df, movies_df = get_data('/Users/edwinjasperjr/Desktop/MRP/Small-ds/ratings.csv', '/Users/edwinjasperjr/Desktop/MRP/Small-ds/movies.csv')
    
    # Initialize the collaborative filtering model
    cf_model = CollaborativeFiltering()
    
    # Convert DataFrame to Surprise dataset
    data = cf_model.load_dataset(ratings_df)

    # Train the model
    cf_model.train(data)
    
    # Evaluate the model
    cf_model.evaluate(data)
    
    # Generate recommendations for a user, now including movie titles
    user_id_for_recommendations = 1 
    n_recommendations = 50  # Number of recommendations to generate
    # Adjust this call to match your updated function that includes movie titles
    top_recommendations = generate_recommendations_with_titles(user_id_for_recommendations, ratings_df, movies_df, cf_model.algo, n_recommendations)
    
    # Print top recommendations with titles
    print(f"Top {n_recommendations} recommendations for user {user_id_for_recommendations}:")
    for movie_id, movie_title, predicted_rating in top_recommendations:
        print(f"Movie: {movie_title}, Movie ID: {movie_id}, Predicted Rating: {predicted_rating}")

if __name__ == '__main__':
    main()
