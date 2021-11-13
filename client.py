import grpc

import calculator_pb2
import calculator_pb2_grpc


# open a grpc channel (Creates an insecure Channel to a server)
channel = grpc.insecure_channel('localhost:50051')

# Create a stub client
stub = calculator_pb2_grpc.CalculatorStub(channel)

# Create a valid request message
number = calculator_pb2.Number(value=78)

# make the call
response = stub.SquareRoot(number)

print(response.value)

