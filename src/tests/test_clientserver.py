# tests/test_mnist_server_client.py
import unittest
import subprocess
import time
from concurrent import futures
import grpc
from src.mnist_server import run_server
from src.mnist_client import run_client
from mnist_pb2 import DataRequest
from mnist_pb2_grpc import MnistServiceStub

class TestMnistServerClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start gRPC server in a separate process
        cls.server_process = subprocess.Popen(['python', 'src/mnist_server.py'])
        # Wait for the server to start
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # Stop the gRPC server
        cls.server_process.terminate()

    def test_mnist_server_client_interaction(self):
        # Test the interaction between the server and client
        channel = grpc.insecure_channel('localhost:50051')
        mnist_service = MnistServiceStub(channel)

        data_request = DataRequest()
        response_stream = mnist_service.GetTrainingSamples(data_request)

        samples_received = 0
        for sample in response_stream:
            label = sample.label
            image_bytes = sample.image
            # Add assertions based on the expected behavior
            self.assertIsNotNone(image_bytes)
            self.assertTrue(0 <= label <= 9)

            samples_received += 1
            if samples_received >= 5:
                break  # Stop after receiving 5 samples for testing purposes

if __name__ == '__main__':
    unittest.main()
