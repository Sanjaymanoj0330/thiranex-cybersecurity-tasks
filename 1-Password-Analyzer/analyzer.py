import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8: score += 1
    else: feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password): score += 1
    else: feedback.append("Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password): score += 1
    else: feedback.append("Add at least one lowercase letter (a-z).")

    if re.search(r"\d", password): score += 1
    else: feedback.append("Add at least one number (0-9).")

    if re.search(r"[ !@#$%^&*(),.?\":{}|<>]", password): score += 1
    else: feedback.append("Add at least one special character.")

    rating = {5: "Very Strong", 4: "Strong", 3: "Medium"}.get(score, "Weak")
    return rating, feedback

if __name__ == "__main__":
    print("--- Password Strength Analyzer ---")
    user_password = input("Enter a password to test: ")
    rating, improvements = check_password_strength(user_password)
    print(f"\nResult: Your password is {rating}")
    if improvements:
        print("Suggestions to make it stronger:")
        for tip in improvements: print(f"- {tip}")