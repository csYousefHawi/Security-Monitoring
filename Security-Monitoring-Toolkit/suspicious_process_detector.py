## This tool lists all currently running processes and identifies if any are running as 'ADMIN' (root/administrator).
## It uses the `psutil` library to list processes and check their user labels.
import psutil
import os

def list_all_processes():
    """Prints a basic list of all running processes."""
    print("--- Current System Processes ---")
    for process in psutil.process_iter(['pid', 'name', 'username']):
        try:
            user = process.info.get('username') or "N/A"
            # Basic labeling for admin vs user
            user_label = 'ADMIN' if user in ['root', 'Administrator'] else 'USER'
            print(f"Process: {process.info['name']}, PID: {process.info['pid']}, User: {user_label}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

def scan_suspicious_processes(cpu_threshold=80.0):
    """Scans for processes exceeding CPU limits or running from temp folders."""
    print(f"\n--- Scanning for Processes over {cpu_threshold}% CPU or in unusual paths ---")
    
    # Common directories where malware often hides
    suspicious_paths = ['\\temp\\', '\\appdata\\local\\temp\\', '/tmp/', '/var/tmp/']
    
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'exe']):
        try:
            name = proc.info['name']
            pid = proc.info['pid']
            cpu = proc.info['cpu_percent']
            exe = proc.info['exe']
            
            # 1. Check for High CPU Usage
            # Note: psutil.cpu_percent might need a second call to be accurate, 
            # but this checks the current process's reported usage.
            if cpu > cpu_threshold:
                print(f"[!] HIGH CPU: {name} (PID: {pid}) is using {cpu}% CPU.")
                
            # 2. Check for execution from typical malware drop folders
            if exe:
                exe_lower = exe.lower()
                for path in suspicious_paths:
                    if path in exe_lower:
                        print(f"[!] SUSPICIOUS PATH: {name} (PID: {pid}) running from {exe}")
                        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

if __name__ == "__main__":
    # Run the basic list
    list_all_processes()
    
    # Run the suspicious activity scan
    scan_suspicious_processes(cpu_threshold=80.0)
