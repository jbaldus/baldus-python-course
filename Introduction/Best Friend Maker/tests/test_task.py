import importlib
from io import StringIO
import sys
import unittest
from unittest.mock import patch
sys.path.append("../../..")
from mock_input_function import MockInputFunction

inputs = [ "Mr. Baldus",
           "kelly green",
           "The Princess Bride",
           "soccer",
           "onions",
           "I.T."]

class TestCase(unittest.TestCase):
    task_name = 'best_friend'

    def setUp(self):
        try:
            # Stores output from print() in actualOutput
            with patch('sys.stdout', new=StringIO()) as self.actualOutput:
                # Loads submission on first test, reloads on subsequent tests
                with MockInputFunction(return_value=inputs):
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
        with open("tests/output.txt") as f:
            expected_output = f.read().strip()

        actual_output = self.actualOutput.getvalue().strip()

        # This does give a confusing start to the error message, but the default for assertIn is worse, as it
        # cannot render <class smth> correctly, and for me, the result is less intriguing this way.
        self.assertEqual(expected_output, actual_output, msg="The actual output did not match the expected output using "
                                                            f" \"{', '.join(inputs)}\" as the inputs. Did you match all the"
                                                             "spaces and punctuation? Did you capitalize the right"
                                                             "words?")
