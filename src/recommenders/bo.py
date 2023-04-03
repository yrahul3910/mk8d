import pandas as pd
from skopt import gp_minimize

from src.configs import get_config
from src.recommenders.base import BaseRecommender


class BORecommender(BaseRecommender):
    __name__ = 'bayesian optimization'

    def _recommend(self):
        result = gp_minimize(
            self._objective,
            dimensions=self.cat_ranges,
            n_calls=10,
            n_initial_points=5,
            verbose=False
        )
        recommendation = pd.Series(
            [result.x[1], result.x[0], result.x[3], result.x[2]], index=['character', 'body', 'tire', 'glider'])
        return get_config(recommendation)
