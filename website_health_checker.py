import requests
import time
import ssl
import socket
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def check_ssl_expiry(url):
    try:
        hostname = urlparse(url).hostname
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=3) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                expiry = cert['notAfter']
                return expiry
    except Exception as e:
        return f"SSL Error: {e}"

def get_title(content):
    try:
        soup = BeautifulSoup(content, 'html.parser')
        title = soup.title.string.strip() if soup.title else ""
        return title
    except Exception:
        return ""

def check_website(url, timeout=5):
    result = {'url': url, 'status': 'down', 'status_code': '', 'response_time': '', 'ssl_expiry': '', 'title': ''}
    try:
        start = time.time()
        resp = requests.get(url, timeout=timeout, allow_redirects=True, verify=True)
        elapsed = round((time.time() - start) * 1000)
        result['status_code'] = resp.status_code
        result['response_time'] = f"{elapsed} ms"
        result['status'] = 'up' if resp.status_code < 400 else 'down'
        result['title'] = get_title(resp.text)
        if url.startswith('https://'):
            result['ssl_expiry'] = check_ssl_expiry(url)
    except requests.exceptions.SSLError as e:
        result['ssl_expiry'] = f"SSL Error: {e}"
    except Exception as e:
        result['status'] = 'down'
        result['status_code'] = str(e)
    return result

def check_bulk_websites(input_file='urls.txt', output_file='health_report.csv'):
    import csv
    with open(input_file) as f:
        urls = [line.strip() for line in f if line.strip()]
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['url', 'status', 'status_code', 'response_time', 'ssl_expiry', 'title'])
        writer.writeheader()
        for url in urls:
            if not url.startswith('http'):
                url = 'http://' + url
            print(f"Checking {url} ...")
            result = check_website(url)
            writer.writerow(result)
            print(result)
    print(f"\nDone! Report saved to {output_file}")

if __name__ == "__main__":
    # To check a single website:
    # print(check_website("https://www.google.com"))

    # To check bulk URLs in a file:
    check_bulk_websites()
