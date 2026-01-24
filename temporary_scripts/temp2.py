from services.transcript_cleaner import remove_operator_and_disclaimer

with open("earnings-call.txt") as f:
    raw_text = f.read()

# Print operator and disclaimer removed
cleaned = remove_operator_and_disclaimer(raw_text)
print(cleaned[:100])