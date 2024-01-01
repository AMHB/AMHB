# Import the os and sys modules
import os
import sys

# Define a function that takes an IP address as an argument and shows the trace route to that IP address
def trace_route(ip_address):
  # Use the os.system() function to execute the traceroute command with the IP address
  # The traceroute command sends packets to the IP address and displays the route and the time taken by each hop
  # The -n option prevents the command from resolving the hostnames of the routers
  os.system(f"tracert {ip_address}")

# Ask the user to enter an IP address
ip_address = input("Please enter an IP address: ")

# Call the trace_route function with the user input
trace_route(ip_address)
