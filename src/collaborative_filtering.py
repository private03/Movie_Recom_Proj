# src/collaborative_filtering.py
from surprise import SVD, Dataset, Reader
from surprise.model_selection import cross_validate, train_test_split

class CollaborativeFiltering:
    def __init__(self, **svd_params):
        self.algo = SVD(**svd_params)


    def load_dataset(self, ratings_df):
        # Define the rating scale
        reader = Reader(rating_scale=(ratings_df['rating'].min(), ratings_df['rating'].max()))
        
        # Load the dataset from the DataFrame
        data = Dataset.load_from_df(ratings_df[['userId', 'movieId', 'rating']], reader)
        return data

    def train(self, data):
        """
        Train the SVD model using the provided dataset.
        :param data: The dataset to train on.
        """
        trainset = data.build_full_trainset()
        self.algo.fit(trainset)

    def evaluate(self, data):
        """
        Evaluate the model's performance using cross-validation.
        :param data: The dataset to evaluate on.
        """
        cross_validate(self.algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

    def predict(self, uid, iid):
        """
        Make a prediction for a given user and item.
        :param uid: The user ID
        :param iid: The item ID
        """
        return self.algo.predict(uid, iid, verbose=True)
    
        
