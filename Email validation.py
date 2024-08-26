import re

def is_valid_email(email):
    # Regular expression for validating an Email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Return True if the email matches the regex, else False
    return re.match(email_regex, email) is not None

# Example usage:
email = "example@domain.com"
if is_valid_email(email):
    print(f"'{email}' is a valid email address.")
else:
    print(f"'{email}' is not a valid email address.")