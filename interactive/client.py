import threading

import example_pb2
import example_pb2_grpc
import grpc


def send_and_receive_messages(stub, client_id):
    for i in range(1, 4):  # Send three messages
        message_content = f"Message {i} from {client_id}"
        request = example_pb2.Request(
            client_id=client_id, message_content=message_content
        )
        responses = stub.StreamMessages(iter([request]))
        for response in responses:
            print(f"Received from server: {response.reply_content}")


def run(client_id):
    channel = grpc.insecure_channel("localhost:50051")
    stub = example_pb2_grpc.MyServiceStub(channel)

    # Start a thread for sending and receiving streaming messages
    send_and_receive_thread = threading.Thread(
        target=send_and_receive_messages, args=(stub, client_id)
    )
    send_and_receive_thread.start()

    # Wait for the send and receive thread to finish
    send_and_receive_thread.join()


if __name__ == "__main__":
    # Start multiple instances of the client with different client_ids
    run("Client1")
    run("Client2")
