from abc import ABC, abstractmethod

import numpy as np
import pandas as pd

from src.configs import get_config


class BaseRecommender(ABC):
    def __init__(self, stats_df: pd.DataFrame):
        self.stats_df = stats_df
        self.categories = self.stats_df.columns[1:5]
        self.cat_ranges = [np.unique(self.stats_df[col]) for col in self.categories]

    @abstractmethod
    def recommend(self):
        raise NotImplementedError

    def _objective(self, *args):
        config = get_config(pd.Series(args[0], index=self.categories).T)
        print()
        print(f'Config: {config}')
        score = int(input('Enter score: '))
        print()
        return score
