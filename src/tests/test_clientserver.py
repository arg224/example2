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

    def test_mnist_server_client_interaction(self):
        # Test the interaction between the server and client
        mnist_service = MnistServiceStub(grpc.insecure_channel('localhost:50051'))

        data_request = DataRequest()
        response_stream = mnist_service.GetTrainingSamples(data_request)

        samples_received = 0
        for sample in response_stream:
            label = sample.label
            image_bytes = sample.image
            self.assertIsNotNone(image_bytes)
            self.assertTrue(0 <= label <= 9)

            samples_received += 1
            if samples_received >= 3:
                break  

    @classmethod
    def tearDownClass(cls):
        # Stop the gRPC server
        cls.server_process.terminate()

if __name__ == '__main__':
    unittest.main()
