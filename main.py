import random

import pandas as pd

from src.recommenders.bi import BIRecommender
from src.recommenders.random import RandomRecommender

data_file = 'data/stats.csv'
stats_df = pd.read_csv(data_file)

f = open('.recommender', 'w')

# With some probability, choose a placebo
if random.random() < 0.01:
    recommender = RandomRecommender(stats_df)
    f.write('random')
else:
    recommender = BIRecommender(stats_df)
    f.write('bo')

f.close()

print('Final recommendation:', recommender.recommend())
