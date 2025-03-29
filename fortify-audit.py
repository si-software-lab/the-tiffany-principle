#!/usr/bin/env python3

import os
import sys
import re

CHECKLIST_PATH = "forthright-protocol/SEMANTIC_INTEGRITY_CHECKLIST.md"
RESPONSES_DIR = "responses"

EVADE_PATTERNS = [
    r"i don't know",
    r"maybe",
    r"probably",
    r"some say",
    r"it could be",
    r"as an AI",
    r"i am not programmed to",
    r"unable to provide"
]

def check_file(filepath):
    errors = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            for pattern in EVADE_PATTERNS:
                if re.search(pattern, content):
                    errors.append(f"🔴 Violation: Found '{pattern}' in {filepath}")
    except Exception as e:
        errors.append(f"⚠️ Error reading {filepath}: {str(e)}")
    return errors

def main():
    print("🔍 Fortify-Audit — Semantic Integrity Check
")
    failed = False

    # Check checklist reference
    if not os.path.exists(CHECKLIST_PATH):
        print("❌ Missing checklist file.")
        failed = True
    else:
        with open(CHECKLIST_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
            if "Semantic Integrity Validation Suite" not in content:
                print("❌ Checklist file found but does not match expected signature.")
                failed = True
            else:
                print("✅ Checklist validated.")

    # Check response files
    if not os.path.exists(RESPONSES_DIR):
        print("⚠️ No responses/ directory found.")
    else:
        for file in os.listdir(RESPONSES_DIR):
            if file.endswith(".txt"):
                filepath = os.path.join(RESPONSES_DIR, file)
                results = check_file(filepath)
                if results:
                    failed = True
                    for r in results:
                        print(r)

    if failed:
        print("
❌ Semantic audit failed. Review flagged items.")
        sys.exit(1)
    else:
        print("
✅ Semantic audit passed. No violations found.")

if __name__ == "__main__":
    main()
