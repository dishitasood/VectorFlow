import services.metadata_extractor 

with open("earnings-call.txt") as f:
    raw_text = f.read()

print(services.metadata_extractor.extract_metadata(raw_text))