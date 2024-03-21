"""
Class to run multiple scenarios
"""

import itertools
import pandas as pd

from classes.model import Model
from classes.scenario import Scenario

class Scenario_runner(object):
    """
    Scenario runner
    """

    def __init__(self, scenarios, prefix=''):
        """constructor class"""

        self.scenarios = scenarios
        self.results = dict()
        self.scenario_values = dict()
        self.prefix = prefix

    def run(self):
        """Run through scenarios"""

        # Generate all scenarios:
        all_scenarios_tuples = [
            x for x in itertools.product(*self.scenarios.values())]
        # Convert list of tuples back to list of dictionaries:
        all_scenarios_dicts = [
            dict(zip(self.scenarios.keys(), p)) for p in all_scenarios_tuples]
        
        # Convert all_scenarios_dicts into a DataFrame for saving
        self.all_scenarios = pd.DataFrame.from_dict(all_scenarios_dicts)
        self.all_scenarios.index.name = 'Scenario'
        self.all_scenarios.to_csv(f'./output/scenario_list_{self.prefix}.csv')

        # Run all scenarios
        for index, scenario_to_run in enumerate(all_scenarios_dicts):
            scenario_to_run['name'] = f'{self.prefix}_{index}'
            # Set up model
            model = Model(
                scenario=Scenario(scenario_to_run),
                geodata=pd.read_csv('processed_data/processed_data.csv'))
            model.run()