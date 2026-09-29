import os
from dotenv import load_dotenv
from instagrapi import Client

# Load local credentials
load_dotenv()

cl = Client()

# Route traffic through the proxy to bypass local Wi-Fi blocks
proxy = os.getenv("PROXY_URL")
if proxy:
    cl.set_proxy(proxy)
    print("Proxy tunnel established.")

try:
    cl.login(os.getenv("INSTAGRAM_USERNAME"), os.getenv("INSTAGRAM_PASSWORD"))
    print("Successfully connected to Instagram past the firewall!")
except Exception as e:
    print(f"Connection failed: {e}")

