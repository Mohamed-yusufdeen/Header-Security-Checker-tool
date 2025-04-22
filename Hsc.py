import requests

# Common security headers to check
security_headers = {
    "Strict-Transport-Security": "Forces HTTPS",
    "Content-Security-Policy": "Prevents XSS",
    "X-Content-Type-Options": "Prevents MIME sniffing",
    "X-Frame-Options": "Prevents clickjacking",
    "Referrer-Policy": "Controls referrer info",
    "Permissions-Policy": "Restricts browser features"
}

def check_security_headers(url):
    print(f"\n🔍 Checking security headers for: {url}\n")
    try:
        response = requests.get(url)
        headers = response.headers

        for header, desc in security_headers.items():
            if header in headers:
                print(f"✅ {header} found - {desc}")
            else:
                print(f"❌ {header} MISSING - {desc}")
    except Exception as e:
        print(f"Error: {e}")

# Example
target = input("Enter a website URL (with http/https): ")
check_security_headers(target)
