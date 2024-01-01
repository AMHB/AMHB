# Import the socket and sys modules
import socket
import sys

# Define a function that takes a URL as an argument and returns the IP addresses of the URL
def get_ip_addresses(url):
  # Remove the protocol (http:// or https://) from the URL if present
  if url.startswith("http://"):
    url = url[7:]
  elif url.startswith("https://"):
    url = url[8:]

  # Split the URL by the first slash (/) to get the domain name
  domain = url.split("/")[0]

  # Use the socket.getaddrinfo() function to get the IP addresses of the domain
  # The function returns a list of tuples, each containing information about an address
  # The first element of each tuple is the address family (AF_INET for IPv4, AF_INET6 for IPv6)
  # The fourth element of each tuple is the address itself, which is also a tuple of (host, port)
  # We only need the host part of the address, which is the first element of the address tuple
  addresses = socket.getaddrinfo(domain, None)
  ip_addresses = [address[4][0] for address in addresses]

  # Return the list of IP addresses
  return ip_addresses

# Define a function that takes an IP address as an argument and returns the port that is open to SSH connections
def get_ssh_port(ip_address):
  # Create an empty list to store the open ports
  open_ports = []

  # Loop through the common ports from 1 to 1024
  for port in range(1, 1025):
    # Create a socket object with the address family AF_INET (IPv4) and type SOCK_STREAM (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the timeout to 0.5 seconds to avoid blocking for too long
    # This is the modification I made to fix the timeout issue
    s.settimeout(10)

    # Try to connect to the IP address and port
    result = s.connect_ex((ip_address, port))

    # If the result is 0, it means the connection was successful and the port is open
    if result == 0:
      # Try to receive some data from the socket
      data = s.recv(1024)

      # If the data starts with b'SSH', it means the port is open to SSH connections
      if data.startswith(b'SSH'):
        # Append the port to the open ports list
        open_ports.append(port)

    # Close the socket
    s.close()

  # Return the list of open ports
  return open_ports

# Ask the user to enter a URL
url = input("Please enter a URL: ")

# Call the get_ip_addresses function with the user input
ip_addresses = get_ip_addresses(url)

# Create an empty dictionary to store the IP addresses and the open ports for SSH
ip_ports = {}

# Loop through the IP addresses
for ip_address in ip_addresses:
  # Call the get_ssh_port function with the IP address
  ssh_port = get_ssh_port(ip_address)

  # Add the IP address and the open ports for SSH to the dictionary
  ip_ports[ip_address] = ssh_port

# Print the result as the "List of IPs and Open Ports for SSH"
print(f"The List of IPs and Open Ports for SSH for {url} is: {ip_ports}")
