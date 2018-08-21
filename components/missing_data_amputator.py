import numpy as np


class MissingDataAmputator:
    def __init__(self, data):
        self.data = data

    def amputate_data(self):
        """Removes all samples that have numpy.NaN as theirs values and returns a new list"""
        return [x for x in self.data if not np.isnan(x)]
