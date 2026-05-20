from src.email_processor import preprocess_email
from src.classifier import classify_email
from src.urgency_detector import detect_urgency
from src.sentiment_engine import analyze_sentiment
from src.task_extractor import extract_tasks
from src.router import assign_department
from src.response_generator import generate_response

from app.interface import display_results

def main():

    print("\n🤖 Intelligent Email Triage System\n")

    email = input("Paste email:\n\n")

    clean_email = preprocess_email(email)

    category = classify_email(clean_email)

    urgency = detect_urgency(clean_email)

    sentiment = analyze_sentiment(clean_email)

    tasks = extract_tasks(clean_email)

    department = assign_department(category)

    response = generate_response(category)

    results = {
        "Category": category,
        "Urgency": urgency,
        "Sentiment": sentiment,
        "Assigned Team": department,
        "Tasks": tasks,
        "Suggested Reply": response
    }

    display_results(results)

if __name__ == "__main__":
    main()
