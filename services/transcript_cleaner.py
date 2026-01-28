import re 

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