from services.metadata_extractor import extract_metadata

with open("earnings-call.txt") as f:
    raw_text = f.read()
print(extract_metadata(raw_text))



