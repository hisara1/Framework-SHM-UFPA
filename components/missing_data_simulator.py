import random
import numpy as np


class MissingDataSimulator:
    """ The simulation of missing data is based on the assumption of MCAR (Missing Completely at Random) """

    def __init__(self, original_data, missing_data_percentage):
        self.original_data = original_data
        self.missing_data_percentage = missing_data_percentage

    def simulate_missing_data(self):
        """Replaces the samples chosen randomly to be removed with numpy.NaN and returns a new list"""
        num_samples_to_be_removed = round(len(self.original_data) * (self.missing_data_percentage / 100))

        new_database = list(self.original_data)

        for i in range(0, num_samples_to_be_removed):
            while True:
                rand_num = random.randint(0, len(new_database) - 1)

                if not np.isnan(new_database[rand_num]):
                    new_database[rand_num] = np.NaN
                    break

        return new_database