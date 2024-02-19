from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Define a list of precompiled patterns to filter
patterns_to_filter = [
    re.compile(r"<script[\s\S]*?>", re.IGNORECASE),
    re.compile(r"javascript:", re.IGNORECASE),
    re.compile(r"onerror", re.IGNORECASE),
    re.compile(r"onload", re.IGNORECASE),
    re.compile(r"alert\(", re.IGNORECASE),
    re.compile(r"confirm\(", re.IGNORECASE),
    re.compile(r"<iframe[\s\S]*?>", re.IGNORECASE),
    re.compile(r"<object[\s\S]*?>", re.IGNORECASE),
    re.compile(r"<embed[\s\S]*?>", re.IGNORECASE)
]

def basic_waf(request_data):
    # Check if the request contains any of the precompiled patterns to filter
    for pattern in patterns_to_filter:
        if pattern.search(request_data):
            return True

    return False

@app.route('/api/protect', methods=['POST'])
def protect():
    try:
        request_data = request.get_json()
        request_text = request_data.get('text', '')

        # Apply basic WAF rules
        if basic_waf(request_text):
            return jsonify({'message': 'Request blocked: contains malicious pattern'}), 403

        return jsonify({'message': 'Request passed WAF'}), 200
    except Exception as e:
        return jsonify({'message': f"Error: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
