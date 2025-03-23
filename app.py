from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/page_content', methods=['POST'])
def page_content():
    """
    Function to retrieve content from a specific page of a textbook.
    Currently returns sample text to confirm functionality.
    """
    data = request.json
    page_number = data.get('page_number')
    
    if not page_number:
        return jsonify({
            "error": "Missing page_number parameter"
        }), 400
    
    try:
        page_number = int(page_number)
    except ValueError:
        return jsonify({
            "error": "page_number must be an integer"
        }), 400
    
    # This is just sample content for testing
    # In a real implementation, this would fetch actual content from a database or file
    sample_content = {
        "page_number": page_number,
        "title": f"Sample Page {page_number}",
        "content": f"This is sample content from page {page_number} of the French textbook. This text would normally contain actual French lessons, vocabulary, or exercises.",
        "vocabulary": [
            {"french": "bonjour", "english": "hello"},
            {"french": "merci", "english": "thank you"},
            {"french": "au revoir", "english": "goodbye"}
        ]
    }
    
    return jsonify(sample_content)

@app.route('/function_gateway', methods=['POST'])
def function_gateway():
    """
    Gateway for OpenAI function calling.
    Receives function calls from OpenAI and routes them to the appropriate function.
    """
    try:
        data = request.json
        
        # Extract function name and arguments
        function_name = data.get('name')
        arguments = data.get('arguments', {})
        
        # Currently we only support the PageContent function
        if function_name == 'PageContent':
            # Call the page_content function with the provided arguments
            page_number = arguments.get('page_number')
            
            if not page_number:
                return jsonify({
                    "error": "Missing page_number parameter"
                }), 400
            
            try:
                page_number = int(page_number)
            except ValueError:
                return jsonify({
                    "error": "page_number must be an integer"
                }), 400
            
            # This is just sample content for testing
            # In a real implementation, this would fetch actual content from a database or file
            sample_content = {
                "page_number": page_number,
                "title": f"Sample Page {page_number}",
                "content": f"This is sample content from page {page_number} of the French textbook. This text would normally contain actual French lessons, vocabulary, or exercises.",
                "vocabulary": [
                    {"french": "bonjour", "english": "hello"},
                    {"french": "merci", "english": "thank you"},
                    {"french": "au revoir", "english": "goodbye"}
                ]
            }
            
            return jsonify(sample_content)
        else:
            return jsonify({
                "error": f"Unknown function: {function_name}"
            }), 400
            
    except Exception as e:
        return jsonify({
            "error": f"Error processing function call: {str(e)}"
        }), 500

@app.route('/', methods=['GET'])
def home():
    return "PageContent API is running. Use POST /page_content with a JSON body containing 'page_number' to get page content."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 