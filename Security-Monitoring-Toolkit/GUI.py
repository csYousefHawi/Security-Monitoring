## This version of the tool uses a graphical user interface (GUI) built with Tkinter.
## The program opens a window with buttons for each task.

## When a button is clicked, the corresponding task runs and the result is displayed in a scrollable text area.
import tkinter as tk
from tkinter import scrolledtext
import sys
import time


try:
    from os_fingerprinting import os_fingerprinting
    from log_file_scanner import log_file_scanner
    from suspicious_process_detector import suspicious_process_detector
    from network_monitor import network_monitor
    from login_activity_analyzer import login_activity_analyzer
except ImportError:
    os_fingerprinting = lambda: print("[+] Running OS Fingerprinting...")
    log_file_scanner = lambda: print("[+] Scanning log files...")
    suspicious_process_detector = lambda: print("[+] Checking processes...")
    network_monitor = lambda: print("[+] Monitoring network...")
    login_activity_analyzer = lambda x: print(f"[+] Analyzing {x}...")

class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget
    def write(self, string):
        self.text_widget.insert(tk.END, string, "green_text")
        self.text_widget.see(tk.END)
    def flush(self):
        pass

class SecurityToolkitGUI:
    def __init__(self, root):
        self.root = root
    
        self.root.title("SECURITY TOOLS") 
        self.root.geometry("1100x750")
        self.root.configure(bg="#05070A")

        # Sidebar
        self.sidebar = tk.Frame(self.root, bg="#05070A", width=320)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=40, pady=30)

        
        lbl_title = tk.Label(
            self.sidebar, 
            text="SECURITY TOOLS", 
            fg="#00F6FF", 
            bg="#05070A", 
            font=('Consolas', 18, 'bold'), 
            pady=20
        )
        lbl_title.pack()

        self.add_brand_button("🎮  OS FINGERPRINTING", lambda: self.run_tool(os_fingerprinting, "EXPLORE PROJECTS"))
        self.add_brand_button("🔍  FILE SCANNER", lambda: self.run_tool(log_file_scanner, "FILE SCANNER"))
        self.add_brand_button("🛡️  SUSPICIOUS PROCESS", lambda: self.run_tool(suspicious_process_detector, "SUSPICIOUS PROCESS"))
        self.add_brand_button("🌐  NETWORK MONITOR", lambda: self.run_tool(network_monitor, "NETWORK MONITOR"))
        self.add_brand_button("🔑  LOGIN ANALYZER", lambda: self.run_tool(lambda: login_activity_analyzer("login.log"), "LOGIN ANALYZER"))

        tk.Label(self.sidebar, bg="#05070A", pady=20).pack()
        self.add_brand_button("🗑️  CLEAR TERMINAL", self.clear_terminal, is_clear=True)

        self.main_area = tk.Frame(self.root, bg="#05070A")
        self.main_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.txt_output = scrolledtext.ScrolledText(
            self.main_area, bg="#000000", fg="#00FF00", 
            font=('Consolas', 11), highlightthickness=2, 
            highlightbackground="#00F6FF", bd=0, padx=15, pady=15
        )
        self.txt_output.pack(fill=tk.BOTH, expand=True)
        self.txt_output.tag_configure("green_text", foreground="#00FF00")

        sys.stdout = StdoutRedirector(self.txt_output)
        print(">> [SYSTEM ONLINE] - SECURITY MODULES READY.")

    def add_brand_button(self, text, command, is_clear=False):
        accent_color = "#FF3E3E" if is_clear else "#00F6FF"
        container = tk.Frame(self.sidebar, bg=accent_color, padx=1, pady=1)
        container.pack(fill=tk.X, pady=8)

        btn = tk.Label(
            container, text=text.upper(), bg="#05070A", fg=accent_color,
            font=('Consolas', 11, 'bold'), padx=15, pady=14, cursor="hand2", anchor="w"
        )
        btn.pack(fill=tk.X)

        btn.bind("<Enter>", lambda e: btn.config(bg=accent_color, fg="#000000"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#05070A", fg=accent_color))
        btn.bind("<Button-1>", lambda e: command())

    def run_tool(self, tool_func, manual_name):
        self.txt_output.insert(tk.END, f"\n[+] INITIATING: {manual_name}...\n", "green_text")
        self.root.update()
        time.sleep(2)
        try:
            tool_func()
        except Exception as e:
            print(f"[!] ERROR: {e}")
        self.txt_output.insert(tk.END, f"[SUCCESS] {manual_name} COMPLETED.\n", "green_text")
        self.txt_output.insert(tk.END, "-"*55 + "\n")

    def clear_terminal(self):
        self.txt_output.delete('1.0', tk.END)
        self.txt_output.insert(tk.END, ">> TERMINAL PURGED. READY FOR NEW COMMANDS...\n", "green_text")

if __name__ == "__main__":
    root = tk.Tk()
    app = SecurityToolkitGUI(root)
    root.mainloop()
