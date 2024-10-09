import psutil
import time

def monitor_resource_usage():
    while True:
        # Get CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)

        # Get memory usage
        mem = psutil.virtual_memory()
        mem_percent = mem.percent

        # Display resource usage
        print(f"CPU Usage: {cpu_percent}%")
        print(f"Memory Usage: {mem_percent}%")

        # Wait for 1 second
        time.sleep(1)

# Start monitoring resource usage
monitor_resource_usage()
