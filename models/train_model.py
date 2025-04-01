import pandas as pd
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
import pickle

# Load dataset
ratings = pd.read_csv('data/ratings.csv')

# Define Reader format
reader = Reader(rating_scale=(0.5, 5.0))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

# Split into train-test
trainset, testset = train_test_split(data, test_size=0.2)

# Train SVD model
model = SVD()
model.fit(trainset)

# Save trained model
with open('models/movie_model.pkl', 'wb') as f:
    pickle.dump(model, f)
