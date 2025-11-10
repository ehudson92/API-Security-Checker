import requests
from urllib.parse import urlparse

# Author: Edward Hudson Jr.
# Description: Checks if a given API endpoint includes key security headers.

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

def check_security_headers(url: str):
    """Check a given API endpoint for common security headers."""
    try:
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = "https://" + url

        response = requests.get(url, timeout=10)
        print(f"\n🔍 Checking: {url}")
        print(f"HTTP Status: {response.status_code}\n")

        for header in SECURITY_HEADERS:
            if header in response.headers:
                print(f"✅ {header}: FOUND")
            else:
                print(f"❌ {header}: MISSING")

    except requests.exceptions.RequestException as e:
        print(f"⚠️  Error: {e}")

if __name__ == "__main__":
    test_url = input("Enter API endpoint URL to check: ").strip()
    check_security_headers(test_url)
