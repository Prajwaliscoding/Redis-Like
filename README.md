# Redis-like Key-Value Store Project

![Status](https://img.shields.io/badge/Status-Active-brightgreen) 
![Python](https://img.shields.io/badge/Python-3.7+-blue)

A lightweight, Redis-like key-value store implementation with persistence, featuring both command-line interface and network server components.

## Features

- In-memory key-value storage with O(1) time complexity for get/set operations
- Persistence using append-only file (AOF) logging
- Network server that accepts SET/GET commands over TCP
- Simple CLI for local key-value operations
- Thread-safe server implementation (one thread per client)

## Architecture

Project Structure
├── key_value_store.py  # Core storage engine with persistence
├── server.py          # Network server component
└── command_line_interface.py  # CLI interface

## Installation

```bash
git clone https://github.com/Prajwaliscoding/Redis-Like.git
cd Redis-Like
``` 

## Usage

1. Command Line Interface

Set a key-value pair:
```bash
python command_line_interface.py --set mykey "my value"
```

Get a value by key:
```bash
python command_line_interface.py --get mykey
```

2. Server Mode

Start the server:
```bash
python server.py
```

Connect to the server using netcat/telnet:
```bash
nc localhost 9999
```

Server commands:

```bash
SET key value - Stores the key-value pair
GET key - Retrieves the value for the given key
```

## Example session:
```bash
$ nc localhost 9999
SET username Prajwal
OK
GET username
"Prajwal"
```

## Implementation Details

1. Core Storage Engine (key_value_store.py)

- Uses Python dictionary for O(1) get/set operations
- Implements persistence through an append-only log file (kv_store.aof)
- On startup, replays all operations from the log to rebuild state
- Each SET operation is immediately written to disk for durability

2. Network Server (server.py)

- TCP server listening on port 9999
- Spawns a new thread for each client connection
- Supports simple text protocol with SET/GET commands
- Thread-safe operations (Python's GIL protects the dictionary access)

3. Command Line Interface (command_line_interface.py)

- Uses argparse for command parsing
- Provides simple --set and --get operations
- Shares the same storage engine with the server

## Performance Characteristics

Operation	Time Complexity	Notes
SET	O(1)	Plus disk I/O for persistence
GET	O(1)	Memory access only

## Limitations

- Single-threaded persistence: The AOF writes are synchronous
- No expiration: Keys don't support TTL/expiration
- Basic protocol: No support for Redis protocol (RESP)
- No replication: Single node only