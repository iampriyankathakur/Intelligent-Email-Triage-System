def assign_department(category):

    routing = {
        "Billing": "Finance Support",
        "Technical Support": "Engineering Support",
        "Sales": "Sales Team",
        "HR": "Recruitment Team",
        "Complaint": "Customer Relations",
        "General": "General Inbox"
    }

    return routing.get(category, "General Inbox")
