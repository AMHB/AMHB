# Import the socket module
import socket

# Define a function that takes a URL as an argument and returns the IP addresses
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

url = input("Plese Insert your URL:  ")
# Test the function with an example URL
#url = "https://www.bing.com"
ip_addresses = get_ip_addresses(url)
print(f"The IP addresses of {url} are: {ip_addresses}")
