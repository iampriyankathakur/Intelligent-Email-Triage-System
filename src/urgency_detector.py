def detect_urgency(text):

    urgent_keywords = [
        "urgent",
        "immediately",
        "asap",
        "critical",
        "emergency"
    ]

    score = 0

    for word in urgent_keywords:
        if word in text.lower():
            score += 1

    if score >= 1:
        return "High"

    return "Normal"
