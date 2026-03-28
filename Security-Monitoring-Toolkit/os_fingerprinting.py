## This tool identifies the system's operating system name and version and some information about processor and machine and other. 
## It uses the platform library to retrieve this information and displays it on the screen.

def os_fingerprinting():
    import platform
    

    os_name = platform.system()
    os_version = platform.version()
    machine = platform.machine()
    processor = platform.processor()
    release = platform.release()
    node = platform.node()


    print("OS Name: " + os_name)
    print("OS Version: " + os_version)
    print("Machine: " + machine)
    print("Processor: " + processor)
    print("Release: " + release)
    print("Node: " + node)


if _name_ == "_main_":
    os_fingerprinting()
