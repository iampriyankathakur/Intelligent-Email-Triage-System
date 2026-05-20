def extract_tasks(text):

    tasks = []

    if "refund" in text.lower():
        tasks.append("Initiate refund review")

    if "interview" in text.lower():
        tasks.append("Schedule interview")

    if "pricing" in text.lower():
        tasks.append("Send pricing brochure")

    if "issue" in text.lower() or "crash" in text.lower():
        tasks.append("Create support ticket")

    return tasks
