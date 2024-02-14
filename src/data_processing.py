# src/data_processing.py

import pandas as pd
import numpy as np

def load_data(ratings_path, movies_path):
    """Load ratings and movies data."""
    ratings = pd.read_csv(ratings_path)
    movies = pd.read_csv(movies_path)
    return ratings, movies

def preprocess_data(ratings, movies):
    """Preprocess data: cleaning, handling missing values, etc."""
    # Fill missing ratings with the average rating, assigning the result directly
    ratings['rating'] = ratings['rating'].fillna(ratings['rating'].mean())
    # Transform dataset into a user-item rating matrix
    ratings_matrix = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)
    return ratings_matrix


def get_data(ratings_path, movies_path):
    # Logic to load data from paths provided
    ratings_df = pd.read_csv(ratings_path)
    movies_df = pd.read_csv(movies_path)
    return ratings_df, movies_df



