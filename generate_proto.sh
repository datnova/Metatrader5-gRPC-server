#!/bin/bash

mkdir -p generated
 python -m grpc_tools.protoc -I=protos --python_out=generated --grpc_python_out=generated protos/*.proto

echo "Proto files have been successfully compiled to Python files in the 'generated' directory."