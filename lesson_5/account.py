import re


def clean_name(name):
    """
    ' sveta ' --> 'Sveta'
    """
    return name.strip().capitalize()

def make_username(first, last):
    """
    'Sveta'  'Svetlaya ' --> sveta_svetlaya
    """
    return f"{first.strip()}_{last.strip()}".lower()

def is_valid_email(email):
    email = email.lower()
    if "@" not in email:
        return False
    domain = email.split("@")[-1]
    return"." in domain

def is_valid_email_secure(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.[a-z]{2,}$"
    return bool( re.match(pattern, email))

def is_valid_password(password):
    return len(password) <= 8

def cut_length(text, limit):
    if len(text) <= limit:
        return text
    return text[:limit]+ "***"

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def get_initials(full_name):
    if not full_name.strip():
        return ValueError("full Name cannot be empty")
    parts = full_name.split()
    initials = [parts[0].upper() for part in parts]
    str = ".".join(initials)+"."
    print(str)
    return str