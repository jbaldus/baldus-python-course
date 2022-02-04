import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch


class MockInputFunction:
    def __init__(self, return_value=None):
        self.return_value = return_value
        self._orig_input_fn = __builtins__['input']

    def _mock_input_fn(self, prompt):
        print(prompt + str(self.return_value))
        return self.return_value

    def __enter__(self):
        __builtins__['input'] = self._mock_input_fn

    def __exit__(self, type, value, traceback):
        __builtins__['input'] = self._orig_input_fn


class TestCase(unittest.TestCase):
    task_name = 'input1'

    def setUp(self):
        try:
            # Stores output from print() in actualOutput
            with patch('sys.stdout', new=StringIO()) as self.actualOutput:
                # Loads submission on first test, reloads on subsequent tests
                with MockInputFunction(return_value="Jason"):
                    if self.task_name in sys.modules:
                        importlib.reload(sys.modules[self.task_name])
                    else:
                        importlib.import_module(self.task_name)
        except NameError as ne:
            pass
        except Exception as e:
            self.fail("There was a problem while loading the solution – {0}. Check the solution for "
                      "IDE-highlighted errors and warnings.".format(str(e)))

    def test_object_type(self):
        expected_output = "What is your name? Jason\nHello, Jason.\n"
        print(f"Actual Output: {self.actualOutput.getvalue()}")
        actual_output = self.actualOutput.getvalue()

        # This does give a confusing start to the error message, but the default for assertIn is worse, as it
        # cannot render <class smth> correctly, and for me, the result is less intriguing this way.
        self.assertEqual(expected_output, actual_output, msg="The statement about the type of float_number is missing "
                                                              "from the output, or the variable's type has changed.")
