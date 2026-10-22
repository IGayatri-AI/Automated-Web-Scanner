import tkinter as tk
from tkinter import ttk, messagebox
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse
from datetime import datetime

SECURITY_HEADERS = {
    "Content-Security-Policy":
        "Helps reduce certain script-injection risks.",
    "X-Content-Type-Options":
        "Helps prevent MIME-type sniffing.",
    "X-Frame-Options":
        "Helps protect against clickjacking.",
    "Strict-Transport-Security":
        "Encourages browsers to use HTTPS.",
    "Referrer-Policy":
        "Controls referrer information shared by browsers."
}


def scan_website():
    url = url_entry.get().strip()

    if not url:
        messagebox.showwarning("Missing URL", "Please enter a website URL.")
        return

    if "://" not in url:
        url = "https://" + url

    parsed = urlparse(url)
    if (parsed.scheme != "https" or not parsed.hostname
            or parsed.username or parsed.password):
        messagebox.showerror(
            "Invalid URL", "Please enter a valid HTTPS website URL."
        )
        return

    host = (parsed.hostname or "").lower()
    if host in ("localhost", "127.0.0.1", "::1") or host.endswith(".local"):
        messagebox.showerror(
            "URL not allowed",
            "Please use a public HTTPS website you are authorized to assess."
        )
        return

    results_box.delete("1.0", tk.END)
    scan_button.config(state="disabled")
    status_label.config(text="Scanning...")
    app.update_idletasks()

    try:
        request = Request(
            url,
            headers={"User-Agent": "Educational-Web-Scanner/1.0"}
        )
        with urlopen(request, timeout=10) as response:
            headers = response.headers
            final_url = response.geturl()
            status_code = response.status

        output = [
            "AUTOMATED WEB SECURITY SCANNER",
            "=" * 40,
            "Original URL: " + url,
            "Final URL: " + final_url,
            "HTTP Status: " + str(status_code),
            "Scan Time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "",
            "1. HTTPS CHECK",
            "-" * 30,
        ]

        if urlparse(final_url).scheme == "https":
            output.append("PASS: Final URL uses HTTPS.")
        else:
            output.append("WARNING: Final URL is not HTTPS.")

        output.extend(["", "2. SECURITY HEADER CHECKS", "-" * 30])
        present = 0
        for header, advice in SECURITY_HEADERS.items():
            if headers.get(header):
                output.append("[PRESENT] " + header)
                present += 1
            else:
                output.append("[MISSING] " + header)
                output.append("Recommendation: " + advice)

        output.extend(["", "3. CORS RESPONSE HEADER CHECK", "-" * 30])
        origin = headers.get("Access-Control-Allow-Origin", "")
        credentials = headers.get("Access-Control-Allow-Credentials", "")

        if origin == "*":
            output.append("WARNING: CORS response allows any origin (*).")
            output.append("Review whether public access is intentional.")
            if credentials.lower() == "true":
                output.append(
                    "Review the CORS configuration carefully. "
                    "This scanner reports headers only; browser enforcement "
                    "and actual exploitability require separate testing."
                )
        elif origin:
            output.append("Allowed origin header: " + origin)
            output.append(
                "Verify that this origin matches the website's security policy."
            )
        else:
            output.append(
                "No Access-Control-Allow-Origin header was found in this response."
            )
            output.append(
                "This alone does not mean CORS is misconfigured."
            )

        output.extend([
            "",
            "4. SUMMARY",
            "-" * 30,
            "Security headers present: " + str(present) + " out of "
            + str(len(SECURITY_HEADERS)),
            "Missing headers are observations, not proof of vulnerabilities.",
            "This educational tool performs basic checks on one HTTP response.",
            "It is not a complete security audit and cannot guarantee website safety."
        ])

        results_box.insert(tk.END, "\n".join(output))
        status_label.config(text="Scan completed.")

    except HTTPError as error:
        messagebox.showerror(
            "Website Response",
            "The website returned HTTP status " + str(error.code) + "."
        )
        status_label.config(text="Website returned an HTTP error.")
    except (URLError, TimeoutError, ValueError) as error:
        messagebox.showerror(
            "Scan Failed",
            "Could not access the website. Check the URL and connection.\n\n"
            + str(error)
        )
        status_label.config(text="Scan failed.")
    except Exception as error:
        messagebox.showerror("Unexpected Error", str(error))
        status_label.config(text="An error occurred.")
    finally:
        scan_button.config(state="normal")


app = tk.Tk()
app.title("Automated Web Security Scanner")
app.geometry("800x600")
app.minsize(600, 450)

title = ttk.Label(
    app, text="Automated Web Security Scanner",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

description = ttk.Label(
    app, text="Basic HTTPS, security-header and CORS checks"
)
description.pack(pady=5)

url_frame = ttk.Frame(app, padding=10)
url_frame.pack(fill="x")
ttk.Label(url_frame, text="Website URL:").pack(side="left", padx=5)

url_entry = ttk.Entry(url_frame)
url_entry.pack(side="left", fill="x", expand=True, padx=5)
url_entry.insert(0, "https://example.com")

scan_button = ttk.Button(
    url_frame, text="Scan Website", command=scan_website
)
scan_button.pack(side="left", padx=5)

results_frame = ttk.LabelFrame(app, text="Security Scan Results", padding=10)
results_frame.pack(fill="both", expand=True, padx=15, pady=10)

results_box = tk.Text(results_frame, wrap="word", font=("Consolas", 10))
scrollbar = ttk.Scrollbar(
    results_frame, orient="vertical", command=results_box.yview
)
results_box.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
results_box.pack(side="left", fill="both", expand=True)

status_label = ttk.Label(app, text="Ready to scan.")
status_label.pack(pady=10)

app.mainloop()
