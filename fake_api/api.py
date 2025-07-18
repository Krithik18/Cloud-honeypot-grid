from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(f"Fake login attempt: {username} / {password}")
    return "Login failed", 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
