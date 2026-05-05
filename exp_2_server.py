#Name of Student: Vidhi Rane
#Div: C   Roll No: 11
#PRN No:72258301L
from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    if n < 0:
        return "Invalid input"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

server = SimpleXMLRPCServer(("localhost", 8000))
print("Server running on port 8000...")

server.register_function(factorial, "factorial")

server.serve_forever()
