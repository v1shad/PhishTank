# PhishTank
Malicious URL Detector

# Malicious URL Detector

## Project Title
**Malicious URL Detector - A Cybersecurity Tool for Phishing Detection**

---

## Overview of the Project

The Malicious URL Detector is a Python-based security tool designed to analyze website links and identify potential phishing attempts before users click on them. This project addresses the critical cybersecurity challenge of **Social Engineering** and **Threat Detection**.

Phishing is one of the most common cyber threats, with **91% of cyberattacks starting with phishing emails**. This tool empowers users to make informed decisions about link safety by analyzing URLs for common red flags associated with malicious websites.

The detector uses **rule-based logic** and **pattern recognition** to calculate a risk score (0-100%) for any given URL, providing users with clear, actionable security recommendations.

### Problem Statement
Users often struggle to identify malicious URLs that appear legitimate at first glance. This tool provides an automated, accessible way to assess URL safety without requiring advanced technical knowledge.

---

## Features

### Core Functionality
✅ **URL Length Analysis** - Detects abnormally long URLs often used in phishing attacks  
✅ **Suspicious Keyword Detection** - Identifies urgent/alarming words like "verify", "secure", "login"  
✅ **Special Character Analysis** - Flags excessive hyphens, @ symbols, and subdomains  
✅ **Domain Reputation Check** - Identifies suspicious TLDs (.xyz, .tk, .ml, etc.)  
✅ **HTTPS Protocol Verification** - Checks if the URL uses secure HTTPS  
✅ **IP Address Detection** - Flags URLs using IP addresses instead of domain names  
✅ **Risk Score Calculation** - Combines all checks into a comprehensive 0-100% risk score  
✅ **Detailed Security Report** - Generates professional, easy-to-understand reports  

### User Experience
- **Interactive Command-Line Interface** - User-friendly prompts and navigation
- **Built-in Test URLs** - Pre-loaded examples for demonstration and testing
- **Multiple Analysis Mode** - Analyze as many URLs as needed in one session
- **Clear Risk Levels** - LOW, MEDIUM, and HIGH risk classifications
- **Actionable Recommendations** - Specific advice based on detected threats

---

## Technologies/Tools Used

### Programming Language
- **Python 3.x** - Core programming language

### Python Standard Libraries
- **`re` (Regular Expressions)** - For pattern matching (IP address detection)
- **Built-in string methods** - For URL parsing and analysis

### Development Tools
- **Text Editor/IDE** - Any Python-compatible editor (VS Code, PyCharm, IDLE, etc.)
- **Command Line/Terminal** - For running the application

### Cybersecurity Concepts Applied
- **Threat Intelligence** - Known bad TLD and domain pattern databases
- **Heuristic Analysis** - Rule-based detection methods
- **Risk Scoring** - Weighted threat assessment algorithms

---

## Steps to Install & Run the Project

### Prerequisites
- Python 3.6 or higher installed on your system
- Basic command-line knowledge

### Installation Steps

#### Step 1: Verify Python Installation
Open your terminal/command prompt and check Python version:
```bash
python --version
```
or
```bash
python3 --version
```

#### Step 2: Download the Project
Save the `url_detector.py` file to your desired directory.

#### Step 3: Navigate to Project Directory
```bash
cd path/to/project/directory
```

#### Step 4: Run the Program
```bash
python url_detector.py
```
or
```bash
python3 url_detector.py
```

### Expected Output
You should see:
```
======================================================================
           WELCOME TO MALICIOUS URL DETECTOR
======================================================================

This tool analyzes URLs for phishing and security threats.
Enter a URL to check, or type "test" for demo URLs, "quit" to exit.

Enter URL (or "test"/"quit"):
```

---

## Instructions for Testing

### Testing Method 1: Using Built-in Test URLs
1. Run the program: `python url_detector.py`
2. Type `test` when prompted
3. Select a test URL (1-5) from the provided list
4. Review the security report generated
5. Compare results across different test URLs

### Testing Method 2: Manual URL Entry
Enter these example URLs manually to test different scenarios:

#### Safe URLs (Expected: LOW RISK)
```
https://www.google.com
https://github.com
https://www.wikipedia.org
https://www.amazon.com
```

#### Moderately Suspicious URLs (Expected: MEDIUM RISK)
```
http://secure-account-login.com
https://paypal-services.net
http://verify-your-account.org
```

#### Highly Suspicious URLs (Expected: HIGH RISK)
```
http://paypal-secure-login-verify.xyz/account
https://secure-bank-account-verification-system-update.tk/login
http://192.168.1.1/secure-login
https://amaz0n-verify-account-update-required.ml/signin
```

### Test Cases & Expected Results

| Test Case | URL Example | Expected Score | Expected Risk Level |
|-----------|-------------|----------------|---------------------|
| Legitimate Site | `https://www.google.com` | 0-15 | LOW RISK |
| No HTTPS | `http://example.com` | 15-25 | LOW-MEDIUM |
| Suspicious TLD | `http://site.xyz` | 25-40 | MEDIUM |
| Many Keywords | `https://secure-login-verify.com` | 40-60 | MEDIUM-HIGH |
| Multiple Red Flags | `http://paypal-secure.tk` | 60-100 | HIGH RISK |

### Verification Steps
For each test, verify that:
1. ✅ The risk score is calculated correctly
2. ✅ The risk level (LOW/MEDIUM/HIGH) matches the score
3. ✅ Detailed analysis shows specific detected threats
4. ✅ Recommendations are appropriate for the risk level
5. ✅ The program doesn't crash on invalid inputs

### Edge Cases to Test
- Empty URL: Press Enter without typing anything
- Very short URL: `http://a.co`
- Very long URL: `https://www.example.com/very/long/path/with/many/segments/...`
- URLs with special characters: `https://example.com/@user/page`
- Malformed URLs: `htp://example` or `www.example.com` (without protocol)

---

## Project Structure

```
malicious-url-detector/
│
├── url_detector.py          # Main program file
├── README.md                # This file - Project documentation
└── test_results.txt         # (Optional) Save your test results here
```

---

## How It Works

### Detection Algorithm
The tool uses a **weighted scoring system** where each security check contributes points to the total risk score:

1. **URL Length** (0-30 points)
   - 0 points: < 54 characters
   - 15 points: 54-75 characters  
   - 30 points: > 75 characters

2. **Suspicious Keywords** (0-40 points)
   - 10 points per keyword detected (max 40)

3. **Special Characters** (0-40 points)
   - 5 points per hyphen (max 20)
   - 25 points per @ symbol
   - 15 points for excessive subdomains

4. **Domain Reputation** (0-30 points)
   - 25 points for suspicious TLDs
   - 30 points for known bad domain patterns

5. **HTTPS Check** (0-15 points)
   - 15 points if not using HTTPS

6. **IP Address** (0-20 points)
   - 20 points if using IP instead of domain

**Total Score:** Sum of all checks (capped at 100)

---

## Limitations & Future Enhancements

### Current Limitations
- Rule-based detection (not machine learning)
- Cannot access live threat intelligence databases
- No real-time web scraping or content analysis
- Cannot detect sophisticated targeted attacks

### Potential Future Improvements
- 🔄 Integration with VirusTotal or Google Safe Browsing API
- 🤖 Machine learning model for improved accuracy
- 🌐 Browser extension for real-time protection
- 📊 Database of user-reported phishing URLs
- 🔍 Domain typosquatting detection (e.g., "paypa1.com")
- 📱 Mobile app version
- 📈 Historical tracking and statistics

---

## Use Cases

### Educational
- Cybersecurity training and awareness programs
- Teaching students about phishing detection
- Demonstrating social engineering tactics

### Personal
- Checking suspicious emails before clicking links
- Verifying URLs shared on social media
- Protecting against online scams

### Professional
- Security awareness training for employees
- Preliminary URL screening in IT departments
- Integration into security protocols

---

## Contributing
This is a capstone project, but suggestions for improvement are welcome! Feel free to:
- Report bugs or issues
- Suggest new detection methods
- Propose feature enhancements

---

## Author
**[Your Name]**  
Cybersecurity Capstone Project  
[Your Institution Name]  
[Date]

---

## License
This project is created for educational purposes as part of a cybersecurity capstone project.

---

## Acknowledgments
- Inspired by real-world phishing detection tools
- Based on cybersecurity best practices and threat intelligence
- Thanks to instructors and peers for feedback and support

---

## Contact
For questions or feedback about this project:
- Email: [your.email@example.com]
- GitHub: [your-github-username]

---

## Disclaimer
This tool is designed for educational purposes and basic threat detection. It should not be relied upon as the sole method of protection against phishing attacks. Always use comprehensive security software and exercise caution when clicking unfamiliar links.

**Remember:** When in doubt, don't click! Verify the sender and context before interacting with any suspicious URL.

---

*Last Updated: [Current Date]*
