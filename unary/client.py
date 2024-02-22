import grpc

import example_pb2
import example_pb2_grpc


def run(client_id):
    channel = grpc.insecure_channel("localhost:50051")
    stub = example_pb2_grpc.MyServiceStub(channel)

    message = example_pb2.Request(
        client_id=client_id, message_content="Hello from client"
    )
    response = stub.SendMessage(message)
    print(f"Received from server: {response.reply_content}")


if __name__ == "__main__":
    # Start multiple instances of the client with different client_ids
    run("Client1")
    run("Client2")
