from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    default_limits=["100 per day", "10 per hour"]
)


class PasswordStrengthChecker:
    def __init__(self):
        pass

    def check_password_strength(self, password):
        # Implement password strength checking algorithm here
        # This is just a placeholder
        return "strong"  # Or "weak" or "medium"


@app.route('/check_password_strength', methods=['POST'])
@limiter.limit("10 per minute")
def check_password_strength():
    data = request.get_json()
    password = data.get('password')

    if not password:
        return jsonify({'error': 'Password not provided'}), 400

    checker = PasswordStrengthChecker()
    strength = checker.check_password_strength(password)

    return jsonify({'strength': strength}), 200



