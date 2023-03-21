
import pandas as pd

from src.recommenders.bi import BIRecommender
from src.recommenders.bo import Myrecommender
from src.recommenders.random import RandomRecommender

data_file = 'data/stats.csv'
stats_df = pd.read_csv(data_file)

recommender = 'bo'
#TODO
player_name = str(input('Enter player\'s name: '))

match recommender:
    case 'bo':
        recommender = Myrecommender(stats_df, player_name)
    case 'bi':
        recommender = BIRecommender(stats_df)
    case 'random':
        recommender = RandomRecommender(stats_df)
    case _:
        raise ValueError('Invalid recommender')

final = recommender.recommend()

print('Final recommendation:', final)
