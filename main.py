#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, jsonify, request

app = Flask(__name__)

def process_text(input_text):
    # Process the input text (capitalize all characters)
    return input_text.upper()

@app.route('/', methods=['POST'])
def index():
    try:
        # Attempt to get JSON data from the request body
        try:
            data = request.get_json(force=True)
        except Exception as e:
            # If JSON parsing fails, try to get form data
            data = request.form

        # Process the text
        processed_text = process_text(data['input_text'])

        # Return the processed text as JSON
        return jsonify({'processed_text': processed_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
