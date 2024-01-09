import grpc
from mnist_pb2 import DataRequest
from mnist_pb2_grpc import MnistServiceStub
from PIL import Image

def run_client():
    channel = grpc.insecure_channel('localhost:50051')
    mnist_service = MnistServiceStub(channel)

    data_request = DataRequest()
    response_stream = mnist_service.GetTrainingSamples(data_request)

    for sample in response_stream:
        label = sample.label
        image_bytes = sample.image

        image = Image.frombytes('L', (28, 28), image_bytes)
        image.save(f"label_{label}.png", "PNG")

        print(f"Received Sample - Label: {label} , Recieved Image - Image: {image}")

if __name__ == '__main__':
    run_client()