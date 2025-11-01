import re

def password_analyzer():
    rules = [
        (lambda p: len(p) >= 8, "At least 8 characters"),
        (lambda p: re.search(r"[A-Z]", p), "At least one uppercase letter"),
        (lambda p: re.search(r"[a-z]", p), "At least one lowercase letter"),
        (lambda p: re.search(r"\d", p), "At least one digit"),
        (lambda p: re.search(r"[!@#$%^&*]", p), "At least one special char"),
    ]

    def evaluate(password):
        passed = [msg for rule, msg in rules if rule(password)]
        failed = [msg for rule, msg in rules if not rule(password)]
        return passed, failed
    
    return evaluate