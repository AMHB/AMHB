#tcp/udp_port_finder
# Import the socket module
import socket

# Define a function that takes an IP address as an argument and returns the open ports
def get_open_ports(ip_address):
  # Create an empty list to store the open ports
  open_ports = []

  # Loop through the common ports from 1 to 1024
  for port in range(1, 1025):
    # Create a socket object with the address family AF_INET (IPv4) and type SOCK_STREAM (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the timeout to 0.1 seconds to avoid blocking for too long
    s.settimeout(0.1)

    # Try to connect to the IP address and port
    result = s.connect_ex((ip_address, port))

    # If the result is 0, it means the connection was successful and the port is open
    if result == 0:
      # Append the port to the open ports list
      open_ports.append(port)

    # Close the socket
    s.close()

  # Return the list of open ports
  return open_ports

# Test the function with an example IP address
ip_address = input('Please insert your IP address: ')
open_ports = get_open_ports(ip_address)
print(f"The open ports of {ip_address} are: {open_ports}")
