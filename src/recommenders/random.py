import random

import pandas as pd

from src.configs import get_config
from src.recommenders.base import BaseRecommender


class RandomRecommender(BaseRecommender):
    __name__ = 'random'
    
    def __init__(self, stats_df):
        super().__init__(stats_df)

    def __recommend(self):
        for _ in range(10):
            # Get random config
            config = [random.choice(x) for x in self.cat_ranges]

            # Get score
            self._objective(config, self.__name__)

        recommendation = pd.Series([random.choice(x) for x in self.cat_ranges],
                                   index=['Character', 'Body', 'Tires', 'Gliders'])
        return get_config(recommendation)
