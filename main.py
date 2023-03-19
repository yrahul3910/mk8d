
import pandas as pd

from src.recommenders.bi import BIRecommender
from src.recommenders.bo import BORecommender
from src.recommenders.random import RandomRecommender

data_file = 'data/stats.csv'
stats_df = pd.read_csv(data_file)

recommender = 'bo'

match recommender:
    case 'bo':
        recommender = BORecommender(stats_df)
    case 'bi':
        recommender = BIRecommender(stats_df)
    case 'random':
        recommender = RandomRecommender(stats_df)
    case _:
        raise ValueError('Invalid recommender')

recommender.recommend()

print('Final recommendation:', recommender.recommend())
