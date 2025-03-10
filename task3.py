import re

def normalize_phone(phone_number: str) -> str:
    sanitized_number = re.sub(r"[^\d+]", "", phone_number)
    if sanitized_number.startswith("380"):
        sanitized_number = "+" + sanitized_number
    elif not sanitized_number.startswith("+"):
        sanitized_number = "+38" + sanitized_number

    return sanitized_number

