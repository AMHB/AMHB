import os
import time

def allocate_memory(gigabytes):
    # Convert gigabytes to bytes
    bytes_to_allocate = int(gigabytes * 1024 * 1024 * 1024)

    # Allocate memory using a bytearray
    memory_block = bytearray(bytes_to_allocate)

    # Print a message to indicate memory allocation
    print(f"Allocated {gigabytes} GB of memory.")

    # Sleep for 10 seconds
    time.sleep(35)

    # Deallocate memory
    del memory_block
    print("Memory deallocated.")

if __name__ == "__main__":
    try:
        # Get user input for desired RAM in GB
        ram_gb = float(input("Enter the amount of RAM (in GB) to allocate: "))
        allocate_memory(ram_gb)
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for RAM (e.g., 2.5 for 2.5 GB).")



time.sleep(10)


def allocate_memory(gigabytes):
    # Convert gigabytes to bytes
    bytes_to_allocate = int(gigabytes * 1024 * 1024 * 1024)

    # Allocate memory using a bytearray
    memory_block = bytearray(bytes_to_allocate)

    # Print a message to indicate memory allocation
    print(f"Allocated {gigabytes} GB of memory.")

    # Sleep for 10 seconds
    time.sleep(15)

    # Deallocate memory
    del memory_block
    print("Memory deallocated.")

if __name__ == "__main__":
    try:
        # Get user input for desired RAM in GB
        ram_gb = float(input("Enter the amount of RAM (in GB) to allocate: "))
        allocate_memory(ram_gb)
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for RAM (e.g., 2.5 for 2.5 GB).")

