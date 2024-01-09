# tests/test_mnist_data_loader.py
import unittest
from src.mnist_data_loader import load_mnist_data

class TestMnistDataLoader(unittest.TestCase):
    def test_load_mnist_data(self):
        mnist_data = load_mnist_data()
        self.assertIsNotNone(mnist_data)
        self.assertTrue(len(mnist_data) > 0)
        # Add more specific assertions based on the expected format of mnist_data

if __name__ == '__main__':
    unittest.main()
