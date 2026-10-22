Automated Web Security Scanner Using Python

Project Description

An educational Python desktop application that checks HTTPS website responses for selected security headers and basic CORS response-header configurations.

Features

- HTTPS URL validation
- Checks five commonly used security headers
- Inspects "Access-Control-Allow-Origin" and "Access-Control-Allow-Credentials" response headers
- Displays findings and basic security recommendations through a graphical interface

Technologies Used

- Python 3
- Tkinter (GUI)
- urllib (HTTP requests)

Requirements

Python 3 with Tkinter support. No third-party Python packages are required.

How to Run

1. Download "CyberSecurity_WebScanner.py".

2. Open the file using Python IDLE or a terminal.

3. Run the following command:
   
   python CyberSecurity_WebScanner.py

4. Enter an HTTPS URL for a website you own or have permission to assess.

5. Click Scan Website and review the results.

Project Files

- "CyberSecurity_WebScanner.py" — Application source code
- "requirements.txt" — Dependency note
- "ProjectReport.docx" — Project report in Word format
- "ProjectReport.pdf" — Project report in PDF format

Dataset

No dataset is required. The application inspects HTTP response headers from the user-provided website at runtime.

Limitations

This project is a learning prototype, not a complete penetration-testing or security-audit tool. It checks a single HTTP response. Missing headers do not automatically indicate a vulnerability, and CORS behavior may depend on the request origin, method, and browser enforcement. Results should be reviewed carefully.

Responsible Use

Only assess websites you own or are explicitly authorized to test. Do not use this tool to attempt exploitation or bypass access controls.

Purpose

This project demonstrates the use of Python, GUI development, HTTP requests, and basic web security concepts for educational purposes.
