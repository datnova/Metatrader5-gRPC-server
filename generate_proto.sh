#!/bin/bash

python -m grpc_tools.protoc -I=protos --python_out=mt5_grpc_proto/mt5_grpc_proto --grpc_python_out=mt5_grpc_proto/mt5_grpc_proto protos/*.proto

# Update import statements in generated Python files
for file in mt5_grpc_proto/*.py; do
    sed -i '' 's/^\(import \)\(.*_pb2 as .*__pb2\)/from . import \2/' "$file"
done

echo "Proto files have been successfully compiled to Python files."