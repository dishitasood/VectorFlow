import re

raw_text = open("earnings-call.txt", "r").read()

def remove_operator_and_disclaimer(text: str) -> str:
    """Removes operator intro and legal disclaimer section"""

    # Remove operator section
    text = re.sub(r"Operator.*?Please go ahead\.", "", text, flags=re.DOTALL | re.IGNORECASE)

    # Remove forward-looking / legal disclaimers
    text = re.sub(r"Our comments and responses.*?actual results could differ materially.*?\.","",text, flags=re.DOTALL | re.IGNORECASE)

    return text.strip()

def extract_prepared_remarks(text: str) -> str:
    """
    Extracts prepared remarks before the Q&A section.
    """

    #Extract the QNA section
    qa_markers = [
        "question-and-answer",
        "q&a",
        "we will now begin the q&a"
    ]

    lower_text = text.lower()

    for marker in qa_markers:
        idx = lower_text.find(marker)
        if idx != -1:
            return text[:idx].strip()

    return text.strip()

def normalize_whitespace(text):
    text = re.sub(r'\r\n', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)    
    text = re.sub(r'[ \t]+', ' ', text)

    return text.strip()

def remove_page_numbers(text):
    return re.sub(r'\nPage \d+\n', '\n', text)

def remove_urls_email(text):
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'\S+@\S+', '', text)
    return text

def remove_copyright(text):
    return re.sub(r'©.*?reserved\.', '', text, flags=re.IGNORECASE)

def remove_forward_looking(text):
    pattern = r'forward[- ]looking statements.*?risks and uncertainties\.'
    return re.sub(pattern, '', text, flags=re.IGNORECASE | re.DOTALL)

def final_cleanup(text):
    text = normalize_whitespace(text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text

