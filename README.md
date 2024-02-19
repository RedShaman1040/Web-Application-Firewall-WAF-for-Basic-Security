### Web Application Firewall (WAF) for Basic Security

### Descripción
This Python-based web application firewall (WAF) provides basic security features to protect web applications from common attacks, such as cross-site scripting (XSS) and SQL injection. It uses regular expressions to detect malicious patterns in incoming requests and blocks them accordingly.

### Características
- **Request Filtering:** Filters incoming requests for malicious patterns.
- **Basic Security Protections:** Protects against common web vulnerabilities, such as XSS and SQL injection.
- **Customizable Rules:** Allows for the addition of custom rules to meet specific security requirements.
- **Error Handling:** Handles exceptions gracefully to prevent server crashes.

### Instalación y Uso

1. Install dependencies:
   ```bash
   pip install Flask
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Access the application at `http://localhost:5000` and use it to protect your web applications.
