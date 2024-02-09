#****** Programmed by Ali Mehrban ******
#****** In this program I monitor the Wifi NIC and demonstrate the network bandwidth
from scapy.all import *
import matplotlib.pyplot as plt
import psutil

# Initialize variables for data rate calculation
start_time = time.time()
total_bytes = {}
ip_curves = {}

def packet_callback(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        payload_size = len(packet)

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # Update data for the specific IP
        if src_ip not in total_bytes:
            total_bytes[src_ip] = 0
            ip_curves[src_ip] = []

        total_bytes[src_ip] += payload_size

        # Calculate traffic throughput (bits per second)
        if elapsed_time > 0:
            throughput_bps = (total_bytes[src_ip] * 8) / elapsed_time
        else:
            throughput_bps = 0

        ip_curves[src_ip].append((elapsed_time, throughput_bps))

        # Plot individual curves
        plt.clf()  # Clear previous plot
        for ip, curve in ip_curves.items():
            x_vals, y_vals = zip(*curve)
            plt.plot(x_vals, y_vals, label=ip)

        plt.xlabel("Time (seconds)")
        plt.ylabel("Traffic Throughput (bps)")
        plt.title("Real-Time Network Traffic by IP")
        plt.legend()
        plt.pause(3)  # Adjust the sampling interval to 3 seconds


# Get the name of the Wi-Fi interface
wifi_interface = None
for interface, addrs in psutil.net_if_addrs().items():
    for addr in addrs:
        if addr.family == socket.AF_INET and interface.startswith("Wi-Fi"):
            wifi_interface = interface
            break
    if wifi_interface:
        break

if wifi_interface:
    print(f"Monitoring Wi-Fi interface {wifi_interface}...")
    sniff(iface=wifi_interface, prn=packet_callback)
else:
    print("No Wi-Fi interface found.")
