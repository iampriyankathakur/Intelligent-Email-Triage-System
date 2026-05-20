def analyze_sentiment(text):

    negative_words = [
        "unhappy",
        "angry",
        "refund",
        "issue",
        "problem",
        "crash"
    ]

    positive_words = [
        "great",
        "love",
        "excellent",
        "thank"
    ]

    neg = sum(word in text.lower() for word in negative_words)
    pos = sum(word in text.lower() for word in positive_words)

    if neg > pos:
        return "Negative"

    if pos > neg:
        return "Positive"

    return "Neutral"
