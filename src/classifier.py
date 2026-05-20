def classify_email(text):

    text = text.lower()

    categories = {
        "Billing": ["charged", "refund", "payment", "subscription"],
        "Technical Support": ["crash", "bug", "error", "issue"],
        "Sales": ["pricing", "demo", "enterprise"],
        "HR": ["interview", "resume", "candidate"],
        "Complaint": ["unhappy", "angry", "bad"]
    }

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in text:
                return category

    return "General"
