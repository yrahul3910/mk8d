from skopt import gp_minimize

from src.recommenders.base import BaseRecommender


class BORecommender(BaseRecommender):
    def __init__(self, stats_df):
        super().__init__(stats_df)

        # Model
        self.optimizer = None

    def recommend(self):
        if self.optimizer is None:
            self.optimizer = gp_minimize(
                self._objective,
                dimensions=self.cat_ranges,
                n_calls=10,
                n_initial_points=5,
                verbose=False
            )
        else:
            self.optimizer.tell(self.last_config, self.last_score)

        return self.optimizer.ask()

    def update(self, config, score):
        self.last_config = config
        self.last_score = score
