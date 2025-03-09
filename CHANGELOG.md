# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-03-09

### Added
- Verbose logging functionality with a new `--verbose` command-line option
- Logging interceptor for detailed request and response logging
- Bump version script for easier version management

### Changed
- Improved README with additional use case diagrams
- Removed excessive MT5 initialization and shutdown code for better performance
- Updated package version to 0.1.1 in setup files

## [0.1.0] - 2024-12-25

### Added
- Initial release of MT5 gRPC Server
- Basic MetaTrader 5 operations support through gRPC
- Protocol buffer definitions for MT5 operations
- Example client implementation
- Basic documentation
- Windows support under Wine for Linux/macOS users

### Dependencies
- Python >=3.8
- gRPC framework
- MetaTrader 5 terminal
- Required Python packages listed in requirements.txt 