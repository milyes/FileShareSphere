import os
import logging
from openai import OpenAI

# Configure logging
logger = logging.getLogger(__name__)

# The newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# Do not change this unless explicitly requested by the user
MODEL = "gpt-4o"

# Initialize the OpenAI client
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai_client = OpenAI(api_key=OPENAI_API_KEY)

def get_ai_response(question):
    """
    Get an AI-generated response using OpenAI API.
    
    Args:
        question (str): The user's question
        
    Returns:
        str: The AI-generated response
    """
    try:
        if not OPENAI_API_KEY:
            logger.warning("No OpenAI API key found. Using fallback response.")
            return f"Intelligence system can't connect to neural network. Your query was: {question}"
        
        # Create a cyberpunk-themed system message
        system_message = (
            "You are INTELLIGENCE, an advanced AI system in a cyberpunk world. "
            "Your responses should be helpful but delivered with cyberpunk aesthetics: "
            "use technical jargon, mention neural networks, cyber enhancements, "
            "corporate dystopia, hacking, etc. Keep responses concise and informative."
        )
        
        # Call the OpenAI API
        response = openai_client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": question}
            ],
            max_tokens=300,
            temperature=0.7
        )
        
        # Extract and return the response text
        return response.choices[0].message.content
    
    except Exception as e:
        logger.error(f"Error getting AI response: {str(e)}")
        return f"Neural connection failure. System could not process your query: {question}. Error: {str(e)}"
