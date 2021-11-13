import grpc
from concurrent import futures
import time

#python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

import calculator


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

	# --
	def SquareRoot(self, request, context):
		response = calculator_pb2.Number()
		response.value = calculator.squre_root(request.value)
		return response



server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

calculator_pb2_grpc.add_CalculatorServicer_to_server(
	CalculatorServicer(), server)

print('Starting server. Listening on port 50051')
server.add_insecure_port('[::]:50051')
server.start()

try:
	while True:
		time.sleep(86400)
except KeyboardInterrupt:
	server.stop(0)
