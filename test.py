import unittest
from calculator import RPNStack

class PRNStackTests(unittest.TestCase):

    """
    Testing of the calculator.
    """

    def setUp(self) -> None:
        """Set up tests"""
        self.calc = RPNStack()

    def test_RPNStack(self):
        """Test constructor"""
        self.assertEqual(0, len(self.calc.items))

    def test_push_items(self):
        """Test push method"""
        self.calc.push(1)
        self.assertEqual(1, len(self.calc.items))
        self.assertEqual([1], self.calc.items)
        self.calc.push(5)
        self.assertEqual(2, len(self.calc.items))
        self.assertEqual([1, 5], self.calc.items)

    def test_pop(self):
        """Test pop method"""
        self.calc.push(4)
        self.calc.push(5)
        self.calc.pop()
        self.assertEqual(1, len(self.calc.items))
        self.assertEqual([4], self.calc.items)
        self.calc.pop()
        self.assertEqual(0, len(self.calc.items))
        self.assertEqual([], self.calc.items)

    def test_isEmpty(self):
        """Test isEmpty method"""
        self.assertEqual(self.calc.isEmpty(), True)

    def test_evaluateExpression(self):
        """Test evaluateExpression method"""
        self.assertEqual(self.calc.evaluateExpression("5 10 *"), 50)
        self.assertEqual(self.calc.evaluateExpression("-3 -2 * 5 +"), 11)


if __name__ == '__main__':
    unittest.main()
