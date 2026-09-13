import tkinter as tk


def check_url():
    url = url_entry.get().lower()

    if url == "":
        result_label.config(text="Please enter a URL")
        return

    suspicious_words = [
        "login",
        "verify",
        "account",
        "password",
        "security",
        "update",
        "confirm"
    ]

    found_words = []

    for word in suspicious_words:
        if word in url:
            found_words.append(word)

    if len(url) > 75:
       if len(url) > 75:
        length_result = "Suspicious - URL is very long"
    else:
        length_result = "Normal"

    if url.startswith("https://"):
        https_result = "Detected"
    else:
        https_result = "Not detected"

    if len(found_words) > 0:
        keyword_result = ", ".join(found_words)
    else:
        keyword_result = "None"

    result_label.config(
        text="URL Received: Yes\n"
             + "URL Length: " + str(len(url)) + " (" + length_result + ")\n"
             + "HTTPS: " + https_result + "\n"
             + "Suspicious Keywords: " + keyword_result
    )

window = tk.Tk()
window.title("Phishing URL Checker")
window.geometry("500x300")


title_label = tk.Label(
    window,
    text="PHISHING URL CHECKER",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=20)


url_entry = tk.Entry(
    window,
    width=50
)
url_entry.pack(pady=10)


check_button = tk.Button(
    window,
    text="CHECK URL",
    command=check_url
)
check_button.pack(pady=10)


result_label = tk.Label(
    window,
    text="Enter a URL to check"
)
result_label.pack(pady=20)


window.mainloop()