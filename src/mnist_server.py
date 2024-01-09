# src/mnist_server.py
import grpc
from concurrent import futures
from mnist_pb2 import DataRequest, Sample
from mnist_pb2_grpc import MnistServiceServicer, add_MnistServiceServicer_to_server
from mnist_data_loader import load_mnist_data

class MnistServiceHandler(MnistServiceServicer):
    def GetTrainingSamples(self, request, context):
        mnist_data = load_mnist_data()
        for image, label in mnist_data:
            yield Sample(image=image.tobytes(), label=label)

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_MnistServiceServicer_to_server(MnistServiceHandler(), server)
    server.add_insecure_port('[::]:50051')
    print('Starting Mnist server on port 50051...')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    run_server()
