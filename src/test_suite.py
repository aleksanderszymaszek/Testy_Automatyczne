import unittest
from src.test_cases import DemoQaTests

class TestSuite(unittest.TestCase):

    def test_main(self):

        self.suite = unittest.TestSuite()
        self.suite.addTest(
            unittest.defaultTestLoader.loadTestsFromTestCase(DemoQaTests)
        )
        runner = unittest.TextTestRunner()
        runner.run(self.suite)


if __name__ == "__main__":
    unittest.main

