import unittest
from calculator import PRNStack

class PRNStackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = PRNStack()

    def test_evaluate(self):
        """Test evaluate method"""
        self.assertEqual(self.calc.evaluateExpression("5 10 *"), 50)
        self.assertEqual(self.calc.evaluateExpression("-3 -2 * 5 +"), 11)

if __name__ == '__main__':
    unittest.main()
