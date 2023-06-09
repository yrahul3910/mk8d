import random

import pandas as pd

from src.configs import get_config
from src.recommenders.base import BaseRecommender


class RandomRecommender(BaseRecommender):
    __name__ = 'random'

    def _recommend(self):
        for _ in range(self.INIT_CONFIGS + self.OPTIMIZER_CONFIGS):
            # Get random config
            config = [random.choice(x) for x in self.cat_ranges]

            # Get score
            self._objective(config, self.__name__)

        recommendation = pd.Series([random.choice(x) for x in self.cat_ranges],
                                   index=['character', 'body', 'tire', 'glider'])
        return get_config(recommendation)
