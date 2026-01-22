def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()-_+=" for char in password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3 or strength == 4:
        return "Moderate"
    else:
        return "Strong"

def main():
    print("Password Strength Checker System")
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(f"Password Strength: {result}")

main()
