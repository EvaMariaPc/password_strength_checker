from words import common_words


class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password
        self.common_words = common_words

    @staticmethod
    def password_strength(self, password):
        # Define criteria for a strong password
        criteria = {
            'length': len(password) >= 8,
            'uppercase': any(char.isupper() for char in password),
            'lowercase': any(char.islower() for char in password),
            'digits': any(char.isdigit() for char in password),
            'special_chars': any(char in r'!@#$%^&*()-_=+[{]}\|;:\'",<.>/?' for char in password)
        }

        # Count how many criteria are met
        strength_meter = sum(criteria.values())

        # Check for common words
        for word in self.common_words:
            if word.lower() in password.lower():
                strength_meter -= 3  # Subtract 3 points for each common word found

        # Interpret the strength level
        if strength_meter == 5:
            return "Very Strong"
        elif strength_meter >= 3:
            return "Strong"
        elif strength_meter >= 2:
            return "Moderate"
        elif strength_meter >= 1:
            return "Weak"
        else:
            return "Very Weak"

    @staticmethod
    def run_tests():
        test_cases = [
            "",
            "password",
            "Password",
            "P@ssword",
            "P@ssword123",
            "P@ssword123!",
            "qweRty",
            "aabbcc",
            "aBc123@",
            "AbCdEfGh1234!@#$",
        ]

        for password in test_cases:
            print(f"Password: '{password}', Strength: {PasswordStrengthChecker.password_strength(password)}")

