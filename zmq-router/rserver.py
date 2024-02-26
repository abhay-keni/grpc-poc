import zmq

context = zmq.Context()
router = context.socket(zmq.ROUTER)
router.bind("tcp://127.0.0.1:5555")

while True:
    identity, message = router.recv_multipart()
    print(f"Received message from {identity.decode()}: {message.decode()}")

    # Process the message (e.g., simulate some work)
    reply = f"Reply to {message.decode()}"

    # Send the reply back to the client identified by its identity
    router.send_multipart([identity, b"", reply.encode()])
