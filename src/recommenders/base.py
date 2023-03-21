from abc import ABC, abstractmethod

import json
import numpy as np
import pandas as pd

from src.configs import get_config


class BaseRecommender(ABC):
    def __init__(self, stats_df: pd.DataFrame, player_name):
        self.stats_df = stats_df
        self.categories = self.stats_df.columns[1:5]
        self.cat_ranges = [np.unique(self.stats_df[col]) for col in self.categories]
        self.score = None
        self.config = None
        self.optimizer_name = None
        self.player_name = player_name

    @abstractmethod
    def __recommend(self, player_name):
        raise NotImplementedError
    
    def recommend(self):
        self.__recommend()
        self.dump_to('output.json', ['config', 'optimizer_name', 'score', ])

    def _objective(self, *args):
        print(args)
        config = get_config(pd.Series(args[0], index=self.categories).T)
        self.optimizer_name = 'bo'
        self.config = config
        print()
        print(f'Config: {config}')
        score = int(input('Enter score: '))
        print()
        self.score = score
        return score
    
    def dump_to(self, filename, var_names):
        temp_dict = {}
        output_dict = {}
        json_data = []
        for var_name in var_names:
            temp_dict[var_name] = getattr(self, var_name)

        output_dict[self.player_name] = temp_dict
        try:
            with open(filename, 'r') as file:
                json_data = json.load(file)
        except json.decoder.JSONDecodeError as e:
            print(f'Error decoding JSON: {e}')

        if len(json_data) > 0:
            json_data.update(output_dict)
            with open(filename, 'w') as file:
                json.dump(json_data, file, indent=4)
        
        else:
            json_data = output_dict
            with open(filename, 'w') as file:
                json.dump(json_data, file, indent=4)
            
