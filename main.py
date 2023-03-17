import pandas as pd

from src.recommenders.random import RandomRecommender

data_file = 'data/stats.csv'
stats_df = pd.read_csv(data_file)

recommender = RandomRecommender(stats_df)
config = recommender.recommend()
