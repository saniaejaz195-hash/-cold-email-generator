def generate_cold_email(company_name, product_or_role, recipient_name):
    email = f"""
Subject: Exploring Opportunities with {company_name}

Dear {recipient_name},

I hope this email finds you well.

My name is Nadia, and I am reaching out to express my interest in {company_name}.
I recently came across your work related to {product_or_role}, and I found it truly impressive.

I believe my skills and passion align well with your organization, and I would love
the opportunity to connect and discuss how I can add value to your team.

Please let me know if you would be open to a short discussion.

Thank you for your time and consideration.

Best regards,  
Nadia
"""
    return email


# Testing directly (optional)
if __name__ == "__main__":
    print(generate_cold_email("TechNova", "AI Developer Role", "John Doe"))
