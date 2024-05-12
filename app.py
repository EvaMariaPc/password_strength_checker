from flask import Flask, request, jsonify
from flask_limiter import Limiter
from password_strength_checker import PasswordStrengthChecker

app = Flask(__name__)
limiter = Limiter(
    app,
    default_limits=["100 per day", "10 per hour"]
)


@app.route('/check_password_strength', methods=['POST'])
@limiter.limit("10 per minute")
def check_password_strength():
    data = request.get_json()
    password = data.get('password')

    if not password:
        return jsonify({'error': 'Password not provided'}), 400

    checker = PasswordStrengthChecker(password)
    strength, _ = checker.password_strength(password)

    return jsonify({'strength': strength}), 200
