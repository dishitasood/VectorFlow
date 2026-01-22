import re
def extract_metadata(raw_text: str) -> str:
    metadata = {}

    # Company INFO 
    metadata["company"] = "Amazon"
    metadata["ticker"] = "AMZN"

    # Extract year and quarter
    match = re.search(r"20\d{2}-Q([1-4])", raw_text)
    if match:
        metadata["year"] = int(match.group(1))
        metadata["quarter"] = f"Qint(match.group(2))"
    
    # Extract topic keywords

    possible_topics = [
    # Administrative & Legal
    "Administrative Introduction",
    "Safe Harbor Statement",
    "Non-GAAP Measures Disclosure",
    
    # CEO's Strategic Section
    "Overall Performance Summary",
    "Strategic Accomplishments & Wins",
    "Business Segment Performance",
    "Macroeconomic Environment Analysis",
    "Competitive Landscape",
    "Strategic Priorities & Investments",
    "Long-term Vision & Market Opportunity",
    
    # CFO's Financial Section
    "Financial Results Overview",
    "Revenue Analysis & Drivers",
    "Profitability & Margin Analysis",
    "Cash Flow & Balance Sheet Health",
    "Capital Allocation Strategy",
    "Forward Guidance & Assumptions",
    
    # Key Performance Indicators
    "Business Metrics & KPIs",
    "Customer Metrics & Behavior",
    "Operational Efficiency Metrics",
    
    # Industry-Specific Focus Areas
    "Industry Trends & Dynamics",
    "Regulatory Environment",
    "Technology & Innovation Updates",
    
    # Operational Details
    "Supply Chain & Operations",
    "Cost Structure & Management",
    "Risk Factors & Challenges",
    
    # Forward-Looking Statements
    "Growth Initiatives & Pipeline",
    "Market Expansion Plans",
    "Investment Priorities",
    
    # Q&A Session Topics
    "Guidance Clarification & Scrutiny",
    "Margin Pressure & Opportunities",
    "Capital Allocation Details",
    "Competitive Positioning",
    "Customer & Demand Trends",
    "One-time Items & Adjustments",
    "Balance Sheet Specifics",
    
    # Closing
    "Closing Remarks",
    "Investor Relations Information"
]

    topics_found = []

    for topic in possible_topics:
        if topic.lower() in raw_text.lower():
            topics_found.append(topic.lower().replace(" ", "-"))
        
    metadata["topics"] = topics_found

    return metadata


