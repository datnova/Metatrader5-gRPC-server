# Metatrader5 RPC Server 🚀

## 📋 Project Description
This project is a gRPC server for interacting with Metatrader 5, designed specifically to provide a convenient way to host an API service on Windows and interact with it using any programming language through gRPC. This approach allows you to build trading applications and services in your preferred language while keeping MetaTrader 5 running on Windows.

## 📄 Use Cases

<div style="display: flex; gap: 20px;">

  <!-- Remote Development Workflow -->
  <div style="flex: 1;">
    <h3>Remote Development Workflow</h3>
    <pre>
┌─────────────────┐     gRPC      ┌──────────────────┐
│   Windows Host  │◄────TCP/IP───►│  Remote Machine  │
│                 │   :50051      │   (Mac/Linux)    │
│ ┌─────────────┐ │               │ ┌──────────────┐ │
│ │MetaTrader 5 │ │               │ │Trading App   │ │
│ └─────┬───────┘ │               │ │(Any Language)│ │
│       │         │               │ └──────────────┘ │
│ ┌─────┴───────┐ │               │                  │
│ │gRPC Server  │ │               │                  │
│ └─────────────┘ │               │                  │
└─────────────────┘               └──────────────────┘
    </pre>
  </div>

  <!-- Multi-Language Integration -->
  <div style="flex: 1;">
    <h3>Multi-Language Integration</h3>
    <pre>
┌────────────────────────────────────────┐
│            gRPC Server                 │
│        ┌─────────────────────┐         │
│        │    MT5 Proto Files  │         │
│        └─────────────────────┘         │
└───────────────┬────────────────────────┘
                │
        Generate│Clients
                │
┌───────────────┼────────────────────────┐
│               ▼                        │
│    ┌──────┐ ┌───┐ ┌────┐ ┌────┐ ┌───┐  │
│    │Python│ │Go │ │Java│ │Node│ │C++│  │
│    └──────┘ └───┘ └────┘ └────┘ └───┘  │
│                                        │
│        Language-Specific Clients       │
└────────────────────────────────────────┘
    </pre>
  </div>

</div>

## 🏗️ Project Structure

The project consists of two main packages:

### 1. MT5 gRPC Proto (`mt5-grpc-proto`)
Protocol Buffers and gRPC service definitions package. Contains the contract between the MT5 gRPC server and its clients. This package provides Python bindings to interact with the server and can be used as a foundation for creating client libraries in other programming languages.

Installation:
```bash
pip install mt5-grpc-proto
```

### 2. MT5 gRPC Server (`mt5-grpc-server`)
The server implementation that interfaces with MetaTrader 5 terminal.

Installation (Windows only or using Wine on Linux/MacOS):
```bash
pip install mt5-grpc-server
```

## ✨ Features
- Account information retrieval
- Trading symbol management
- Sending and checking trading orders
- Market data acquisition
- Position management
- Retrieving trade and order history
- Terminal information retrieval

## 💡 Key Benefits
- Run MetaTrader 5 on Windows while accessing it from any OS
- Build trading applications in any language that supports gRPC
- Create client libraries based on the project's proto files for your preferred programming language
- High-performance binary protocol communication
- Bi-directional streaming capabilities
- Type-safe API interface

## 🖥️ Server Usage

### Basic Start
```bash
mt5-grpc-server
```
The server will start on default port 50051 and host 0.0.0.0

### Secure Connection
```bash
mt5-grpc-server --host 127.0.0.1 --port 50052 --secure --cert-file server.crt --private-key-file server.key
```

### Command-line Options
- `--host HOST`: Host address to bind the server to (default: "0.0.0.0")
- `--port PORT`: Port number to listen on (default: 50051)
- `--secure`: Enable secure connection with SSL/TLS
- `--cert-file FILE`: Path to the SSL certificate file (required if --secure is used)
- `--private-key-file FILE`: Path to the private key file (required if --secure is used)

## 🛠️ Development Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/Metatrader5-gRPC-server.git
cd Metatrader5-gRPC-server
```

## 🔄 Generating Proto Files
To regenerate proto files during development, use:
```bash
./generate_proto.sh
```

## 🐧 Running Under Wine (Linux, MacOS)
If you need to run the server on Linux:
```bash
./start_server_under_wine.sh
```

## 📚 Usage Examples
See `client_example.py` for client code examples. You can implement clients in any language that supports gRPC.

## 📄 License
MIT License

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. 