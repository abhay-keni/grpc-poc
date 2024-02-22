from concurrent import futures

import grpc

import example_pb2
import example_pb2_grpc


class MyServiceServicer(example_pb2_grpc.MyServiceServicer):
    def StreamMessages(self, request_iterator, context):
        for request in request_iterator:
            client_id = request.client_id
            message_content = request.message_content
            response_content = f"Server received from {client_id}: {message_content}"
            response = example_pb2.Response(
                client_id=client_id, reply_content=response_content
            )
            yield response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started listening on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
