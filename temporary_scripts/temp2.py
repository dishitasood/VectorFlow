from services.transcript_cleaner import (
    remove_operator_and_disclaimer,
    extract_prepared_remarks
)

with open("earnings-call.txt") as f:
    raw = f.read()

cleaned = remove_operator_and_disclaimer(raw)
prepared = extract_prepared_remarks(cleaned)

print(prepared[-1000:])