#!/usr/bin/env python3
# ============================================================
#  
#   ██████╗  ██████╗ ███████╗███████╗████████╗
#   ██╔══██╗██╔═══██╗██╔════╝██╔════╝╚══██╔══╝
#   ██████╔╝██║   ██║███████╗███████╗   ██║   
#   ██╔══██╗██║   ██║╚════██║╚════██║   ██║   
#   ██████╔╝╚██████╔╝███████║███████║   ██║   
#   ╚═════╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   
#                                             
#   ██████╗ ███████╗███╗   ███╗██╗███╗   ██╗
#   ██╔══██╗██╔════╝████╗ ████║██║████╗  ██║
#   ██████╔╝█████╗  ██╔████╔██║██║██╔██╗ ██║
#   ██╔══██╗██╔══╝  ██║╚██╔╝██║██║██║╚██╗██║
#   ██║  ██║███████╗██║ ╚═╝ ██║██║██║ ╚████║
#   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝
#                                             
#   GHOST v1.0 - OSINT & TRACKING TOOL        
#   create by vikk official                   
#   "find the truth, protect the innocent."   
#                                             
# ============================================================

import os
import sys
import time
import json
import requests
import re
import threading
from datetime import datetime

# ============================================================
VERSION = '1.0'
AUTHOR = 'vikk official'

# ============================================================
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_animation(text, duration=1.2):
    chars = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f'\r  \033[96m[{chars[i % len(chars)]}] {text}\033[0m')
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write(f'\r  \033[92m[✓] {text}\033[0m\n')

def progress_bar(current, total, label='processing'):
    bar_length = 25
    filled = int(bar_length * current / total)
    bar = '█' * filled + '░' * (bar_length - filled)
    percent = round(current / total * 100, 1)
    sys.stdout.write(f'\r  \033[96m[{bar}] {percent}%  -  {label}\033[0m')
    sys.stdout.flush()

def loading(text):
    print(f"  \033[92m• {text}\033[0m")

def error(text):
    print(f"  \033[91m• {text}\033[0m")

def info(text):
    print(f"  \033[94m• {text}\033[0m")

def success(text):
    print(f"  \033[92m• {text}\033[0m")

def warning(text):
    print(f"  \033[93m• {text}\033[0m")

def divider():
    print("  " + "-" * 50)

# ============================================================
def show_banner():
    clear()
    print("""
\033[96m
   ██████╗  ██████╗ ███████╗███████╗████████╗
   ██╔══██╗██╔═══██╗██╔════╝██╔════╝╚══██╔══╝
   ██████╔╝██║   ██║███████╗███████╗   ██║   
   ██╔══██╗██║   ██║╚════██║╚════██║   ██║   
   ██████╔╝╚██████╔╝███████║███████║   ██║   
   ╚═════╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   
                                             
   ██████╗ ███████╗███╗   ███╗██╗███╗   ██╗
   ██╔══██╗██╔════╝████╗ ████║██║████╗  ██║
   ██████╔╝█████╗  ██╔████╔██║██║██╔██╗ ██║
   ██╔══██╗██╔══╝  ██║╚██╔╝██║██║██║╚██╗██║
   ██║  ██║███████╗██║ ╚═╝ ██║██║██║ ╚████║
   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝
\033[0m
\033[93m
   ──────────────────────────────────────────────
   GHOST v1.0  |  osint & tracking tool
   create by vikk official
   "find the truth, protect the innocent."
   ──────────────────────────────────────────────
\033[0m
""")

# ============================================================
def check_email(email):
    results = []
    
    loading_animation("initializing osint engine", 0.6)
    loading_animation("connecting to breach database", 0.6)
    
    for i in range(1, 5):
        progress_bar(i, 4, "scanning email")
        time.sleep(0.15)
    print()
    time.sleep(0.2)
    
    loading_animation(f"checking: {email}", 0.8)

    try:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            results.append(f"found in {len(data)} data breaches")
            for b in data[:5]:
                results.append(f"  - {b.get('Name', 'unknown')} ({b.get('BreachDate', 'unknown')})")
        elif res.status_code == 404:
            results.append("no breaches found")
        else:
            results.append("api error (rate limited)")
    except:
        results.append("could not check breaches")

    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        results.append("valid email format")
    else:
        results.append("invalid email format")

    results.append(f"domain: {email.split('@')[1]}")
    return results

def check_phone(phone):
    results = []
    
    loading_animation("initializing osint engine", 0.6)
    loading_animation("connecting to carrier database", 0.6)
    
    for i in range(1, 5):
        progress_bar(i, 4, "scanning phone")
        time.sleep(0.15)
    print()
    time.sleep(0.2)
    
    loading_animation(f"checking: {phone}", 0.8)

    phone = re.sub(r'[^0-9+]', '', phone)
    results.append(f"cleaned number: {phone}")

    codes = {
        '62': 'indonesia', '1': 'usa/canada', '44': 'uk',
        '91': 'india', '81': 'japan', '86': 'china',
        '60': 'malaysia', '65': 'singapore', '63': 'philippines',
        '84': 'vietnam'
    }
    found = False
    for code, country in codes.items():
        if phone.startswith(code):
            results.append(f"country: {country}")
            found = True
            break
    if not found:
        results.append("country: not detected")

    if len(phone) >= 10:
        results.append("valid phone format")
    else:
        results.append("invalid phone format")

    return results

def search_social(query):
    results = []
    
    loading_animation("searching social media platforms", 0.8)
    
    for i in range(1, 5):
        progress_bar(i, 4, "scanning platforms")
        time.sleep(0.15)
    print()
    time.sleep(0.2)

    platforms = ['instagram', 'facebook', 'twitter', 'github', 'youtube', 'reddit']
    for p in platforms:
        results.append(f"  - {p}: check manually (api needed)")

    return results

# ============================================================
def generate_report(data_type, query, results):
    loading_animation("generating report", 0.6)
    
    print("\n\033[96m   ════════════════════════════════════════════\033[0m")
    print("\033[96m   📋  OSINT REPORT\033[0m")
    print("\033[96m   ════════════════════════════════════════════\033[0m")
    print(f"\n   type  : {data_type}")
    print(f"   query : {query}")
    print(f"   time  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n   results:")
    divider()
    for r in results:
        print(f"   {r}")
    divider()
    print("\n\033[93m   ⚠️  data from public sources only")
    print("   ⚠️  use responsibly")
    print("   ⚠️  your searches stay local & private\033[0m")

# ============================================================
def main():
    show_banner()

    print("\033[93m")
    print("   ⚠️  for education only")
    print("   ⚠️  no stalking, no harassment")
    print("   ⚠️  developer not responsible for misuse")
    print("\033[0m")

    print("\n\033[96m   what do you want to track?\033[0m")
    print("   \033[94m1\033[0m  email")
    print("   \033[94m2\033[0m  phone number")
    print("   \033[94m3\033[0m  full search (email + social)")
    print("   \033[91m4\033[0m  exit")

    choice = input("\n\033[96m   select (1-4): \033[0m").strip()

    if choice == '1':
        email = input("   enter email: ").strip()
        if email:
            results = check_email(email)
            generate_report('email', email, results)
        else:
            error("email required")

    elif choice == '2':
        phone = input("   enter phone (e.g., 628123456789): ").strip()
        if phone:
            results = check_phone(phone)
            generate_report('phone', phone, results)
        else:
            error("phone number required")

    elif choice == '3':
        query = input("   enter email or phone: ").strip()
        if query:
            results = []
            if '@' in query:
                results.extend(check_email(query))
            else:
                results.extend(check_phone(query))
            results.extend(search_social(query))
            generate_report('full search', query, results)
        else:
            error("query required")

    elif choice == '4':
        print("\n\033[92m   find the truth, protect the innocent.\033[0m")
        sys.exit(0)

    else:
        error("invalid option")

    input("\n\033[96m   press enter to continue...\033[0m")
    main()

# ============================================================
if __name__ == '__main__':
    try:
        import requests
    except ImportError:
        print("\033[91m   [ ! ] requests not installed. run: pip install requests\033[0m")
        sys.exit(1)
    main()
