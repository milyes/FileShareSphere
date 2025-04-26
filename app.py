import os
import logging
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from services.openai_service import get_ai_response

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "cyberpunk-intelligence-secret")
CORS(app)

@app.route("/", methods=["GET"])
def index():
    """Render the main page."""
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    """Process a question and return an AI-generated response."""
    try:
        data = request.get_json()
        
        if not data:
            logger.error("No JSON data received")
            return jsonify({"error": "No data provided"}), 400
        
        question = data.get("question", "")
        
        if not question:
            logger.error("No question provided")
            return jsonify({"error": "No question provided"}), 400
        
        logger.debug(f"Received question: {question}")
        
        # Get response from OpenAI
        response = get_ai_response(question)
        
        return jsonify({
            "response": response
        })
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({
            "error": "An error occurred while processing your request",
            "details": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
