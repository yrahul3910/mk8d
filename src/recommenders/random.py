import random

import pandas as pd

from src.configs import get_config
from src.recommenders.base import BaseRecommender


class RandomRecommender(BaseRecommender):
    def __init__(self, stats_df):
        super().__init__(stats_df)

    def recommend(self):
        for _ in range(10):
            # Get random config
            config = [random.choice(x) for x in self.cat_ranges]

            # Get score
            self._objective(config)

        recommendation = pd.Series([random.choice(x) for x in self.cat_ranges],
                                   index=['Character', 'Body', 'Tires', 'Gliders'])
        return get_config(recommendation)
