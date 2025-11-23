def lengthcheck(url):
    length = len(url)
    if length > 75:
        return {'score': 30, 'detail': f'URL is unusually long ({length} chars)'}
    elif length > 54:
        return {'score': 15, 'detail': f'URL is moderately long ({length} chars)'}
    return {'score': 0, 'detail': 'URL length is normal'}

def suspicious(url):
    keywords = ['login', 'verify', 'secure', 'account', 'update',
                'banking', 'confirm', 'suspend', 'locked', 'alert',
                'password', 'urgent', 'validate', 'credential']

    url_lower = url.lower()
    matches = [word for word in keywords if word in url_lower]
    score = min(len(matches) * 10, 40)

    if matches:
        detail = f'Found suspicious keywords: {", ".join(matches)}'
    else:
        detail = 'No suspicious keywords found'

        return {'score': score, 'detail': detail}

def spchars(url):
    risk = 0
    details = []

    hyphen_count = url.count('-')
    if hyphen_count > 0:
        hyphen_score = min(hyphen_count * 5, 20)
        risk += hyphen_score
        details.append(f'{hyphen_count} hyphens detected')

    at_count = url.count('@')
    if at_count > 0:
        risk += at_count * 25
        details.append(f'{at_count} @ symbols found (unusual)')

    try:
        domain_part = url.split('//')[1].split('/')[0]
        subdomain_count = domain_part.count('.')
        if subdomain_count > 3:
            risk += 15
            details.append(f'{subdomain_count} subdomains (excessive)')
    except:
        pass

    detail = ', '.join(details) if details else 'Normal character usage'
    return {'score': min(risk, 40), 'detail': detail}

def baddomain(url):

    bad_tlds = ['.xyz', '.top', '.tk', '.ml', '.ga', '.cf', '.pw', '.cc']
    suspicious_domains = ['paypal-secure', 'amazon-verify', 'microsoftonline',
        'apple-id', 'account-update', 'secure-login']

    url_lower = url.lower()

    for tld in bad_tlds:
        if tld in url_lower:
            return {'score': 25, 'detail': f'Suspicious TLD detected: {tld}'}

    for domain in suspicious_domains:
        if domain in url_lower:
            return {'score': 30, 'detail': f'Suspicious domain pattern: {domain}'}

    return {'score': 0, 'detail': 'Domain appears legitimate'}

def httpcheck(url):

    if not url.lower().startswith('https://'):
        return {'score': 15, 'detail': 'Not using secure HTTPS protocol'}
    return {'score': 0, 'detail': 'Uses secure HTTPS protocol'}

def ipcheck(url):

    import re
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    if re.search(ip_pattern, url):
            return {'score': 20, 'detail': 'Uses IP address instead of domain name'}
    return {'score': 0, 'detail': 'Uses proper domain name'}

def riskscore(url):

    checks = {
    'URL Length': lengthcheck(url),
        'Suspicious Keywords': suspicious(url),
        'Special Characters': spchars(url),
            'Domain Reputation': baddomain(url),
            'HTTPS Protocol': httpcheck(url),
            'IP Address Check': ipcheck(url)
            }

    total_score = sum(check['score'] for check in checks.values())
    total_score = min(total_score, 100)

    return total_score, checks

def report(url, score, checks):

        if score < 30:
            risk_level = 'LOW RISK'
            status = '✓'
            advice = 'This URL appears relatively safe, but always verify the sender.'
        elif score < 60:
            risk_level = 'MEDIUM RISK'
            status = '⚠'
            advice = 'Exercise caution. Verify the domain carefully before clicking.'
        else:
            risk_level = 'HIGH RISK'
            status = '✗'
            advice = 'DANGER! This URL shows multiple red flags. DO NOT CLICK.'

        print('\n' + '='*70)
        print('               MALICIOUS URL DETECTOR - SECURITY REPORT')
        print('='*70)
        print(f'\nURL Analyzed: {url}')
        print(f'\n{status} RISK SCORE: {score}/100')
        print(f'{status} RISK LEVEL: {risk_level}')
        print(f'\n{advice}')

        print('\n' + '-'*70)
        print('DETAILED ANALYSIS:')
        print('-'*70)

        for check_name, result in checks.items():
            status_icon = '✓' if result['score'] == 0 else '⚠' if result['score'] < 20 else '✗'
            print(f'\n{status_icon} {check_name}: [{result["score"]} points]')
            print(f'  → {result["detail"]}')

        print('\n' + '='*70 + '\n')

def main():

    print('\n' + '='*70)
    print('           WELCOME TO MALICIOUS URL DETECTOR')
    print('='*70)
    print('\nThis tool analyzes URLs for phishing and security threats.')
    print('Enter a URL to check, or type "test" for demo URLs, "quit" to exit.\n')

    test_urls = {
        '1': ('Safe - Google', 'https://www.google.com'),
        '2': ('Safe - GitHub', 'https://github.com'),
        '3': ('Suspicious - Fake PayPal', 'http://paypal-secure-login-verify.xyz/account'),
        '4': ('Suspicious - Long URL', 'https://secure-bank-account-verification-system-update.tk/login'),
        '5': ('Suspicious - IP Address', 'http://192.168.1.1/secure-login')
    }

    while True:
        user_input = input('Enter URL (or "test"/"quit"): ').strip()

        if user_input.lower() == 'quit':
            print('\nThank you for using Malicious URL Detector!')
            break

        elif user_input.lower() == 'test':
            print('\nTEST URLs:')
            for key, (name, url) in test_urls.items():
                print(f'{key}. {name}')
                print(f'   {url}')

                choice = input('\nSelect a test URL (1-5): ').strip()
                if choice in test_urls:
                    url = test_urls[choice][1]
                    print(f'\nAnalyzing: {url}')
                else:
                    print('Invalid choice. Please try again.')
                    continue

        elif user_input:
                url = user_input
        else:
            print('Please enter a valid URL.')
            continue

        score, checks = riskscore(url)
        report(url, score, checks)

        continue_check = input('Analyze another URL? (y/n): ').strip().lower()
        if continue_check != 'y':
            print('\nThank you for using Malicious URL Detector!')
            break

if __name__ == '__main__':
    main()