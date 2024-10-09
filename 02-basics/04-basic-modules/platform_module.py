# Import the platform module to access system-related information
import platform

# 1. Get the operating system type (e.g., Linux, Windows, Darwin for macOS)
def get_system():
    """Returns the type of operating system using platform.system()"""
    return platform.system()

# 2. Get detailed system information (uname: OS, node name, release, version, machine, processor)
def get_uname():
    """Returns detailed system information using platform.uname()"""
    return platform.uname()

# 3. Get the machine type (e.g., x86_64, AMD64)
def get_machine():
    """Returns the machine type using platform.machine()"""
    return platform.machine()

# 4. Get the operating system release (e.g., version number of the OS)
def get_release():
    """Returns the OS release version using platform.release()"""
    return platform.release()

# 5. Get the system architecture (e.g., ('64bit', 'ELF'))
def get_architecture():
    """Returns the system architecture using platform.architecture()"""
    return platform.architecture()

# 6. Get the processor type (e.g., x86 Family, ARM)
def get_processor():
    """Returns the processor type using platform.processor()"""
    return platform.processor()

# 7. Get the network name of the machine (hostname)
def get_node():
    """Returns the network node name (hostname) using platform.node()"""
    return platform.node()

# Main function to demonstrate the use of platform module methods
if __name__ == "__main__":
    # 1. Get the operating system type
    print(f"Operating System: {get_system()}")

    # 2. Get detailed system information
    uname_info = get_uname()
    print(f"System Information (uname): {uname_info}")

    # 3. Get the machine type
    print(f"Machine Type: {get_machine()}")

    # 4. Get the OS release version
    print(f"OS Release Version: {get_release()}")

    # 5. Get the system architecture
    architecture = get_architecture()
    print(f"System Architecture: {architecture[0]} ({architecture[1]})")

    # 6. Get the processor type
    print(f"Processor Type: {get_processor()}")

    # 7. Get the network node name (hostname)
    print(f"Node Name (Hostname): {get_node()}")
