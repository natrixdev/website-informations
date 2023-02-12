import socket
import time

def get_domain_name(url):
    try:
        host_name = socket.gethostbyname(url)
        return host_name
    except:
        return None

def get_ping(host):
    try:
        ping =  str(round(time.time() * 1000 - time.time() * 1000, 2)) + " ms"
        return ping
    except:
        return None

def display_info(url):
    print("Website information:")
    print("-------------------")
    print(f"URL: {url}")
    host_name = get_domain_name(url)
    print(f"Domain Name: {host_name}")
    ping = get_ping(host_name)
    print(f"Ping: {ping}")
    print("-------------------")

display_info("www.example.com")
