# streamlit_app.py
import streamlit as st
from collaborative_filtering import CollaborativeFiltering
from data_processing import get_data
from recommendation_generator import generate_recommendations_with_titles  # Updated import

# Load your data from your specific directory path
ratings_df, movies_df = get_data('path/to/ratings.csv', 'path/to/movies.csv')

# Initialize and load your trained collaborative filtering model
# Assuming the model is already trained
cf_model = CollaborativeFiltering()
# cf_model.load('path/to/trained_model')  # Assuming a method to load a pre-trained model

# Convert DataFrame to Surprise dataset
data = cf_model.load_dataset(ratings_df)

# Train the model
cf_model.train(data)  # Ensure this line is present to train your model


# Streamlit UI
st.title('Movie Recommendation System')

# User ID input
user_id = st.number_input('Enter User ID', min_value=1, value=1, step=1)

# Number of recommendations
n_recommendations = st.slider('Number of Recommendations', min_value=5, max_value=20, value=10)

# Generate recommendations button
if st.button('Generate Recommendations'):
    with st.spinner('Generating Recommendations...'):
        recommendations_with_titles = generate_recommendations_with_titles(
            user_id, ratings_df, movies_df, cf_model.algo, n_recommendations
        )

        # Display recommendations with titles
        st.header('Top Recommendations')
        for movie_id, title, predicted_rating in recommendations_with_titles:
            st.write(f"{title} (ID: {movie_id}) - Predicted Rating: {predicted_rating:.2f}")
