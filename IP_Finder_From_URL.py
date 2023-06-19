import socket

def get_ip_addresses(url):
    try:
        # Get IP addresses associated with the URL
        ip_addresses = socket.gethostbyname_ex(url)[2]
        return ip_addresses
    except socket.gaierror:
        return []

# Example usage
url = input("Enter the URL: ")
ip_addresses = get_ip_addresses(url)
print("IP Address(es):", ip_addresses)