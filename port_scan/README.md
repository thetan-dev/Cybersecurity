# Simple Port and Network Scanner

This project is a basic **network utility** written in Python that demonstrates two core concepts:

1. A simple **TCP port scanner** for a given hostname.  
2. Basic **IP address and subnet handling** using the `IPy` library.[web:170][web:181]

---

## What the Script Does

- Uses Python’s `socket` library to attempt TCP connections to a small set of well‑known ports (22, 80, 443) on a target such as `stackoverflow.com` and prints whether each port appears **OPEN** or **CLOSED**.[web:170][web:173]  
- Uses `IPy`’s `IP` class to:
  - Represent and display a single IP address (e.g., `192.168.1.1`).  
  - Represent a network (e.g., `192.168.1.0/29`) and iterate through each IP address in that subnet.[web:181]

This makes it a simple example of how port scanning and IP subnet iteration work in Python.

---

## Features

- **Port scanning:**
  - Scans a fixed list of ports: `22` (SSH), `80` (HTTP), `443` (HTTPS).  
  - Uses `socket.socket(AF_INET, SOCK_STREAM)` and `settimeout(1)` to attempt fast TCP connections.  
  - Prints a line for each port indicating whether the connection succeeded or timed out.[web:170][web:173]

- **IP address utilities:**
  - Creates an `IP` object for a single address (`192.168.1.1`) and prints it.  
  - Creates an `IP` object for a network (`192.168.1.0/29`) and loops over all IPs in that range, printing each one.[web:181]

---

## Requirements

- **Python** 3.x  
- **Libraries:**
  - Standard library: `socket`  
  - Third‑party: `IPy` (for IP and network handling)[web:181]

Install `IPy` with:

pip install IPy

text

---

## How It Works (High Level)

1. **Port scan section**
   - The script defines a list of ports and a `targetip` hostname.  
   - For each port:
     - Creates a TCP socket.
     - Sets a 1‑second timeout on connection attempts.
     - Calls `connect((targetip, port))`:
       - If the connection succeeds before timeout, the port is printed as **OPEN**.
       - If a timeout occurs, it prints **CLOSED**.[web:170][web:173][web:183]
     - The socket is closed in a `finally` block to release resources.

2. **IP address section**
   - Constructs `IP('192.168.1.1')` to demonstrate working with a single IP object.  
   - Constructs `IP('192.168.1.0/29')` to represent a small network and iterates through it in a `for` loop, printing each address in that subnet.[web:181][web:178]

---

## Usage Notes and Ethics

- This script is intended as an **educational tool** for understanding basic port scanning and IP/subnet iteration in Python.[web:173][web:183]  
- Only scan **hosts and networks you own or have explicit permission to test**. Unauthorized port scanning can violate acceptable‑use policies and local laws.