Automated Web Security Scanner Using Python
Project description
An educational desktop application that checks an HTTPS website response for selected security headers and basic CORS response-header configuration.
Features
HTTPS URL validation
Checks for five commonly used security headers
Inspects Access-Control-Allow-Origin and Access-Control-Allow-Credentials response headers
Displays findings and basic recommendations in a graphical interface
Technologies
Python 3
Tkinter (GUI)
urllib (HTTP requests)
Requirements
Python 3 with Tkinter support. No third-party Python packages are required.
How to run
Download CyberSecurity_WebScanner.py.
Open it using Python IDLE or run python CyberSecurity_WebScanner.py in a terminal.
Enter an HTTPS URL for a website you own or have permission to assess.
Click Scan Website and review the output.
Files
CyberSecurity_WebScanner.py — application source code
requirements.txt — dependency note
ProjectReport.docx — project report
ProjectReport.pdf — PDF copy of the report
Limitations
This is a learning prototype, not a complete penetration-testing or security-audit tool. It checks a single HTTP response. Missing headers do not automatically prove a vulnerability, and CORS behavior can depend on request origin, method, and browser enforcement. Results should be interpreted by a knowledgeable reviewer.
Responsible use
Only assess websites that you own or are explicitly authorized to test. Do not use this tool to attempt exploitation or bypass access controls.
Dataset
No dataset is required; the application inspects HTTP response headers from the user-provided website at runtime.
