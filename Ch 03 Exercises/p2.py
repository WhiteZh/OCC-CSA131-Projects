def email_checker(email: str) -> bool:
    if email.count('@') != 1:
        return False
    
    if not '.' in email[email.find('@'):]:
        return False
    
    if ' ' in email:
        return False
    
    return True

email = input("Your email: ").strip()

print(f"Your email is {'' if email_checker(email) else 'not '}valid")

    