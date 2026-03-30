## This version of the tool is run in the command line interface (CLI).
## The user interacts with the program by choosing a task number from a list.
## The program then runs the corresponding task and displays the result in the terminal.

from os_fingerprinting import os_fingerprinting
from log_file_scanner import log_file_scanner
from suspicious_process_detector import list_all_processes, scan_suspicious_processes
from network_monitor import network_monitor
from login_activity_analyzer import login_activity_analyzer
import time
def main_menu():
    while True:
         
        print("\n=== Security Monitoring Toolkit ===")
        print("1. OS Fingerprinting")
        print("2. File Scanner for Security Logs")
        print("3. Suspicious Process Detector")
        print("4. Network Connection Monitor")
        print("5. Login Activity Analyzer")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        time.sleep(2)
        if choice == '1':
            os_fingerprinting() 
        elif choice == '2':
            log_file_scanner()       
        elif choice == '3':
         list_all_processes()
         scan_suspicious_processes()  
        elif choice == '4':
            network_monitor()    
        elif choice == '5':
            login_activity_analyzer("login.log")    
        elif choice == '0':
            print("Exiting the toolkit...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()
