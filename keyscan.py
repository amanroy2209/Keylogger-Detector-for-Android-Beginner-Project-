import os

keywords = [
    "key", "log", "spy", "monitor", "record",
    "stealth", "logger", "capture", "keyboard",
    "tracker", "remote", "control"
]

print("🔍 Scanning installed apps...\n")

apps = os.popen("pm list packages").read().lower()

found = False

for key in keywords:
    if key in apps:
        print(f"⚠ Suspicious keyword found: {key}")
        found = True

if not found:
    print("✅ No suspicious apps detected.")