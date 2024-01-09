import unittest
from src.mnist_data_loader import load_mnist_data

class TestMnistDataLoader(unittest.TestCase):
    # Test the load mnist data function individually
    def test_load_mnist_data(self):
        mnist_data = load_mnist_data()
        self.assertIsNotNone(mnist_data)
        self.assertTrue(len(mnist_data) > 0)

if __name__ == '__main__':
    unittest.main()
