from skopt import gp_minimize

from src.configs import get_config
from src.recommenders.base import BaseRecommender


class BORecommender(BaseRecommender):
    def recommend(self):
        result = gp_minimize(
            self._objective,
            dimensions=self.cat_ranges,
            n_calls=10,
            n_initial_points=5,
            verbose=False
        )

        return get_config(result.x)
