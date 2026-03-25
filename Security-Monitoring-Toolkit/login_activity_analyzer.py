

def login_activity_analyzer(log_file="login.log"):
    import random
    from datetime import datetime
    import re
    # --- جزء توليد سجلات وهمية ---
    users = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
    entries = 10  # عدد السجلات اللي نضيفها

    for _ in range(entries):
        user = random.choice(users)
        status = random.choice(["login successful", "login failed"])
        ip = f"192.168.1.{random.randint(1, 20)}"
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = f"{date} - INFO - User {status} from IP {ip}\n"
        with open(log_file, "a") as f:
            f.write(record)

    print(f"{entries} login records added to {log_file}")

    
    successful = 0
    failed = 0
    failed_ips = {}

    with open(log_file, 'r') as f:
        for line in f:
            line_lower = line.lower()
            if 'login successful' in line_lower:
                successful += 1
            elif 'login failed' in line_lower:
                failed += 1
                ip_match = re.search(r'\b\d{1,3}(\.\d{1,3}){3}\b', line)
                if ip_match:
                    ip = ip_match.group()
                    failed_ips[ip] = failed_ips.get(ip, 0) + 1

    print(f"\n--- Login Analysis ---")
    print(f"Successful logins: {successful}")
    print(f"Failed logins: {failed}")
    print("\nSuspicious IPs (multiple failed attempts):")
    for ip, count in failed_ips.items():
        if count > 2: 
            print(f"{ip} - {count} failed attempts")
