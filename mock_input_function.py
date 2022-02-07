import collections.abc
import itertools


class MockInputFunction:
    def __init__(self, return_value=None, cycle=True):
        self.cycle = cycle
        self.return_value = return_value
        self._orig_input_fn = __builtins__['input']

    def _mock_input_fn(self, prompt):
        return_value = self.return_value
        print(prompt + str(return_value))
        return return_value

    def __enter__(self):
        __builtins__['input'] = self._mock_input_fn

    def __exit__(self, type, value, traceback):
        __builtins__['input'] = self._orig_input_fn

    @property
    def return_value(self):
        if isinstance(self._return_value, str) or not isinstance(self._return_value, collections.abc.Iterable):
            return self._return_value
        else:
            return next(self._return_value)

    @return_value.setter
    def return_value(self, value):
        if isinstance(value, str) or not isinstance(value, collections.abc.Iterable):
            self._return_value = value
        elif isinstance(value, collections.abc.Iterable):
            if self.cycle:
                self._return_value = itertools.cycle((x for x in value))
            else:
                self._return_value = (x for x in value)
