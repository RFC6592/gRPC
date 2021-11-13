import grpc

import calculator_pb2
import calculator_pb2_grpc


# open a grpc channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub client
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
number = calculator_pb2.Number(value=78)

# make the call
response = stub.SquareRoot(number)

print(response.value)

