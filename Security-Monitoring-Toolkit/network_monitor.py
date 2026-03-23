## This tool monitors active network connections and lists listening ports.
## It uses the `psutil` library to retrieve and display network connection details.
def network_monitor():
    import psutil

    print("Active Network Connections:")
    for conn in psutil.net_connections():
        print(f"Local: {conn.laddr} <-> Remote: {conn.raddr}, Status: {conn.status}")

    print("\nListening Ports:")
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'LISTEN':
            print(f"Port: {conn.laddr.port}, PID: {conn.pid}")
