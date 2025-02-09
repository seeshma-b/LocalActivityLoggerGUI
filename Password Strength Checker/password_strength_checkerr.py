def check_password_strength_strict(password):
    # criteria for password strength
    length_requirement = 12
    complexity_requirements = {
        'uppercase': False,
        'lowercase': False,
        'digit': False,
        'special_char': False
    }
    special_characters = "!@#$%^&*()_-+=[]{}|\\;:'\",.<>/?"
    
    # Checking for empty password
    if not password:
        return "Um, the password cannot be empty."
    
    # Checking length
    if len(password) < length_requirement:
        return "Password length should be at least {} characters.".format(length_requirement)
    
    # Checking character types
    for char in password:
        if char.isupper():
            complexity_requirements['uppercase'] = True
        elif char.islower():
            complexity_requirements['lowercase'] = True
        elif char.isdigit():
            complexity_requirements['digit'] = True
        elif char in special_characters:
            complexity_requirements['special_char'] = True
    
    # Checking if all complexity requirements are met
    if all(complexity_requirements.values()):
        return "Password is strong! Woohoo!!!."
    else:
        requirements_not_met = [key for key, value in complexity_requirements.items() if not value]
        return "Hmmm...The password needs at least one {}.".format(" and ".join(requirements_not_met))

# Testing the password policies
if __name__ == "__main__":
    try:
        password = input("Please enter your password: ")
        strength = check_password_strength_strict(password)
        print(strength)
    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")
    except Exception as e:
        print("An error has occurred:", str(e))
