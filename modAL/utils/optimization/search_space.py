import numpy as np


class SearchSpace:
    __slots__ = ('space', 'var_names')

    def __init__(self, *args, **kwargs):
        self.space = list(args) + list(kwargs.values())
        self.var_names = list(kwargs.keys())

    def __getitem__(self, idx):
        try:
            item = self.space[idx]()
        except TypeError:
            if isinstance(idx, list):
                item = np.array([self.space[i]() for i in idx])
            else:
                raise TypeError('SearchSpace indices must be integers or lists')

        return item

    def numpy_sample(self):
        return np.array([dist() for dist in self.space])
