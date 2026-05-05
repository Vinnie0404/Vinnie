#Name of Student: Vidhi Rane
#Div: C   Roll No: 11
#PRN No:72258301L

import random

# Simulated servers
servers = {
    "Server1": 0,
    "Server2": 0,
    "Server3": 0
}

# Simulated client requests
requests = ["Req1", "Req2", "Req3", "Req4", "Req5", "Req6"]

print("Client Requests:", requests)

# -------------------------------
# 1. Round Robin
# -------------------------------
print("\n--- Round Robin ---")
rr_servers = list(servers.keys())
rr_index = 0

for req in requests:
    server = rr_servers[rr_index]
    print(f"{req} -> {server}")
    rr_index = (rr_index + 1) % len(rr_servers)

# -------------------------------
# 2. Random Allocation
# -------------------------------
print("\n--- Random Allocation ---")

for req in requests:
    server = random.choice(list(servers.keys()))
    print(f"{req} -> {server}")

# -------------------------------
# 3. Least Connections
# -------------------------------
print("\n--- Least Connections ---")

# Reset loads
server_load = {s: 0 for s in servers}

for req in requests:
    # Find server with minimum load
    server = min(server_load, key=server_load.get)
    
    print(f"{req} -> {server}")
    
    # Increase load
    server_load[server] += 1

print("\nFinal Server Loads:", server_load)

