import grpc
from concurrent import futures
from mnist_pb2 import Sample
from mnist_pb2_grpc import MnistServiceServicer, add_MnistServiceServicer_to_server
from mnist_data_loader import load_mnist_data

class MnistServiceHandler(MnistServiceServicer):
    def GetTrainingSamples(self):
        mnist_data = load_mnist_data()
        for image, label in mnist_data:
            image_bytes = bytes(image)
            yield Sample(image=image_bytes, label=label)

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_MnistServiceServicer_to_server(MnistServiceHandler(), server)
    server.add_insecure_port('[::]:50051')
    print('Starting the mnist server on 50051...')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    run_server()
