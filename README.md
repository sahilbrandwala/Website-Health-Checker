# 🌐 Website Health Checker

A production-ready, bulk and single website health checker in Python.  
Checks status code, uptime, response time, SSL certificate validity, and page title.

---

## ✨ Features

- ✅ Checks if sites are up or down  
- 🔍 HTTP status code & response time  
- 🔒 SSL certificate expiry date (for HTTPS)  
- 🏷️ Fetches web page title  
- 📝 CSV report output for bulk checks  

---

## 🚀 Quick Start

### 1. Install Requirements

```bash
pip install -r requirements.txt

```
### 2. Add URLs
Create a file named urls.txt with one URL per line, for example:


https://www.google.com
https://expired.badssl.com
http://example.com
yourdomain.com


### 3. Run the Script

python website_health_checker.py


### 4. Check the Output
The script creates a health_report.csv with results, like:

url	status	status_code	response_time	ssl_expiry	title
https://www.google.com	up	200	203 ms	...	Google
https://badssl.com	down	...	...	SSL Error: ...	

🧠 How It Works
Uses requests for HTTP(S) check and timing.

Uses ssl/socket for certificate expiry checks.

Uses BeautifulSoup for extracting page title.

🛠️ Customization
Change or add URLs in urls.txt.

Adjust CSV output fields in the script as needed.

📜 License
Open source — use, modify, and share!

Made with ❤️ for webmasters and developers.