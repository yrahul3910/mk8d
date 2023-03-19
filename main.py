import random

import pandas as pd

from src.recommenders.bo import BORecommender
from src.recommenders.random import RandomRecommender

data_file = 'data/stats.csv'
stats_df = pd.read_csv(data_file)

f = open('.recommender', 'w')

# With some probability, choose a placebo
if random.random() < 0.5:
    recommender = RandomRecommender(stats_df)
    f.write('random')
else:
    recommender = BORecommender(stats_df)
    f.write('bo')

f.close()

recommender.recommend()
