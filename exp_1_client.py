#Name of Student: Vidhi Rane
#Div: C   Roll No: 11
#PRN No:72258301L
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

num = int(input("Enter a number: "))

result = proxy.factorial(num)

print("Factorial is:", result)
