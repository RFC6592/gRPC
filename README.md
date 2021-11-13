# gRPC

+ Pour générer 'calculator_pb2' & 'calculator_pb2_grpc' à partir du schéma 'calculator.proto'

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto