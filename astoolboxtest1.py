import os
import time
import random
import hashlib
import requests
import phonenumbers
import whois
from datetime import datetime
from phonenumbers import geocoder, carrier
from colorama import Fore, init

init(autoreset=True)
GREEN = Fore.GREEN

DISCORD_EPOCH = 1420070400000

# INSERT YOUR API KEY HERE
VT_API_KEY = "PUT_YOUR_VIRUSTOTAL_API_KEY_HERE"


# -----------------
# CLEAR
# -----------------

def clear():
    os.system("cls" if os.name == "nt" else "clear")


# -----------------
# LOADING
# -----------------

def loading():

    chars = ["#", "%", "@", "$", "&"]

    print(GREEN + "\n[AS‑OSINT] Loading...\n")

    for i in range(10):
        bar = "".join(random.choice(chars) for _ in range(25))
        print(GREEN + "[" + bar + "]")
        time.sleep(0.05)

    print(GREEN + "\nModule Ready\n")


# -----------------
# DISCORD LOOKUP
# -----------------

def discord_lookup():

    loading()

    snowflake = input(GREEN + "Discord ID: ")

    try:

        snowflake = int(snowflake)

        timestamp = ((snowflake >> 22) + DISCORD_EPOCH) / 1000
        created = datetime.utcfromtimestamp(timestamp)

        print(GREEN + "\nAccount Created:", created, "UTC")
        print(GREEN + f"Profile: https://discord.com/users/{snowflake}")

    except:
        print(GREEN + "Invalid ID")

    input(GREEN + "\nENTER to continue")


# -----------------
# PHONE LOOKUP
# -----------------

def phone_lookup():

    loading()

    number = input(GREEN + "Phone number (+country): ")

    try:

        parsed = phonenumbers.parse(number)

        print(GREEN + "\nCountry:", geocoder.description_for_number(parsed, "en"))
        print(GREEN + "Carrier:", carrier.name_for_number(parsed, "en"))
        print(GREEN + "Valid:", phonenumbers.is_valid_number(parsed))

    except:
        print(GREEN + "Invalid number")

    input(GREEN + "\nENTER to continue")


# -----------------
# IP LOOKUP
# -----------------

def ip_lookup():

    loading()

    ip = input(GREEN + "IP Address: ")

    try:

        data = requests.get(f"http://ip-api.com/json/{ip}").json()

        for k, v in data.items():
            print(GREEN + f"{k}: {v}")

    except:
        print(GREEN + "Lookup failed")

    input(GREEN + "\nENTER to continue")


# -----------------
# USERNAME SCAN
# -----------------

def username_scan():

    loading()

    username = input(GREEN + "Username: ")

    sites = {

        "Instagram": f"https://instagram.com/{username}",
        "TikTok": f"https://tiktok.com/@{username}",
        "Reddit": f"https://reddit.com/user/{username}",
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "YouTube": f"https://youtube.com/@{username}",
        "Twitch": f"https://twitch.tv/{username}",
        "Pinterest": f"https://pinterest.com/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}"
    }

    print(GREEN + "\nScanning sites...\n")

    for site, url in sites.items():

        try:

            r = requests.get(url)

            if r.status_code == 200:
                print(GREEN + f"[FOUND] {site}: {url}")
            else:
                print(GREEN + f"[X] {site}")

        except:
            print(GREEN + f"{site}: error")

    input(GREEN + "\nENTER to continue")


# -----------------
# DOMAIN LOOKUP
# -----------------

def domain_lookup():

    loading()

    domain = input(GREEN + "Domain: ")

    try:

        info = whois.whois(domain)

        print(GREEN + "Registrar:", info.registrar)
        print(GREEN + "Created:", info.creation_date)
        print(GREEN + "Expires:", info.expiration_date)

    except:
        print(GREEN + "WHOIS failed")

    input(GREEN + "\nENTER to continue")


# -----------------
# VIRUSTOTAL URL CHECK
# -----------------

def vt_url_scan():

    loading()

    url = input(GREEN + "URL to scan: ")

    headers = {"x-apikey": VT_API_KEY}

    data = {"url": url}

    response = requests.post(
        "https://www.virustotal.com/api/v3/urls",
        headers=headers,
        data=data
    )

    if response.status_code == 200:
        print(GREEN + "\nURL submitted to VirusTotal successfully.")
        print(GREEN + "Check report in your VirusTotal dashboard.")
    else:
        print(GREEN + "Submission failed")

    input(GREEN + "\nENTER to continue")


# -----------------
# ROBLOX LOOKUP
# -----------------

def roblox_lookup():

    loading()

    username = input(GREEN + "Roblox username: ")

    try:

        r = requests.post(
            "https://users.roblox.com/v1/usernames/users",
            json={"usernames":[username]}
        ).json()

        user_id = r["data"][0]["id"]

        print(GREEN + "User ID:", user_id)
        print(GREEN + f"Profile: https://www.roblox.com/users/{user_id}/profile")

    except:
        print(GREEN + "User not found")

    input(GREEN + "\nENTER to continue")


# -----------------
# MENU
# -----------------

def menu():

    while True:

        clear()

        print(GREEN + """
AS‑OSINT TOOLKIT
----------------

1  Discord ID Lookup
2  Phone Number Lookup
3  IP Address Lookup
4  Username Scanner
5  Domain Lookup
6  VirusTotal URL Check
7  Roblox User Lookup

0  Exit
""")

        choice = input(GREEN + "Select option: ")

        if choice == "1":
            discord_lookup()

        elif choice == "2":
            phone_lookup()

        elif choice == "3":
            ip_lookup()

        elif choice == "4":
            username_scan()

        elif choice == "5":
            domain_lookup()

        elif choice == "6":
            vt_url_scan()

        elif choice == "7":
            roblox_lookup()

        elif choice == "0":
            break


menu()