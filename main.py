from flask import Flask, request, jsonify, render_template
from password_strength_checker import PasswordStrengthChecker

app = Flask(__name__)


# Define route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        password = request.form['password']

        if not password:
            return render_template('pass.html', error='Password not provided')

        # Instantiate PasswordStrengthChecker
        checker = PasswordStrengthChecker(password)

        # Assess password strength
        password_strength = checker.password_strength(password)



# Define route for checking password strength
@app.route('/check_password_strength', methods=['POST'])
def check_password_strength():
    data = request.get_json()
    password = data.get('password')

    if not password:
        return jsonify({'error': 'Password not provided'}), 400

    # Instantiate PasswordStrengthChecker
    checker = PasswordStrengthChecker(password)

    # Assess password strength
    strength, points = checker.assess_strength()

    return jsonify({'strength': strength, 'points': points}), 200


def run_main():
    pass


# Your feedback gathering logic here
def gather_feedback():
    pass


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
