def generate_response(category):

    responses = {
        "Billing":
            "We apologize for the inconvenience. Our finance team is reviewing your request.",

        "Technical Support":
            "Our engineering support team is investigating the issue.",

        "Sales":
            "Thank you for your interest. Our sales team will contact you shortly.",

        "HR":
            "Thank you for reaching out. Our recruitment team will follow up soon.",

        "Complaint":
            "We appreciate your feedback and will address your concerns promptly.",

        "General":
            "Thank you for contacting us."
    }

    return responses[category]
