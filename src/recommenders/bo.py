from abc import ABC, abstractmethod
import pandas as pd
from skopt import gp_minimize

from src.configs import get_config
from src.recommenders.base import BaseRecommender


class BORecommender(ABC):
    @abstractmethod
    def _BaseRecommender__recommend(self):
        pass

class Myrecommender(BaseRecommender):
    __name__ = 'bayesian optimization'

    def _BaseRecommender__recommend(self):
        result = gp_minimize(
            self._objective,
            dimensions=self.cat_ranges,
            n_calls=10,
            n_initial_points=5,
            verbose=False
        )
        recommendation = pd.Series(result.x, index=['Character', 'Body', 'Tires', 'Gliders'])
        return get_config(recommendation)
