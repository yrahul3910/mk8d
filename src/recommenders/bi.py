
import numpy as np
import pymc3 as pm

from src.configs import get_config
from src.recommenders.base import BaseRecommender


class BIRecommender(BaseRecommender):
    def __init__(self, stats_df):
        super().__init__(stats_df)
        self.weights = []
        self.scores = []

    def recommend(self):
        for _ in range(5):
            # Get random config
            w = np.random.normal(0, 1, 12)
            self.weights.append(w)
            idx = np.sum(w * self.stats_df.iloc[:, 5:17], axis=1).argmax()
            config = self.stats_df.iloc[idx, 1:5].astype(int)

            # Get score
            score = self._objective(config)
            self.scores.append(score)

        for i in range(6):
            mu_w = np.mean(self.weights)
            sigma_w = np.std(self.weights)
            mu_x = np.mean(self.scores)
            sigma_x = np.std(self.scores)

            with pm.Model() as model:
                # Prior for the weights w_i
                weights = pm.Normal('weights', mu=mu_w, sigma=sigma_w, shape=12)

                # Prior for the covariates x_i
                covariates = pm.Normal('covariates', mu=mu_x,
                                       sigma=sigma_x, shape=(len(self.scores), 12))

                # Likelihood for the observed score
                score = pm.Deterministic('score', pm.math.dot(weights, covariates.T))
                pm.Normal('score_obs', mu=score,
                                      sigma=0.1, observed=self.scores)

            with model:
                idata = pm.sample(1000, tune=2000, cores=1, return_inferencedata=True)

            w = idata.posterior['weights'].mean(dim='draw')[0].values
            self.weights.append(w)
            idx = np.sum(w * self.stats_df.iloc[:, 5:17], axis=1).argmax()
            config = self.stats_df.iloc[idx, 1:5].astype(int)

            if i == 5:
                return get_config(config)

            score = self._objective(config)
            self.scores.append(score)
