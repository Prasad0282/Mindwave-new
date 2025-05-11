# from flask import Flask, render_template, request, jsonify
# import os
# from dotenv import load_dotenv
# from chatbot.chatbot import Chatbot  
# from flask_cors import CORS



# # Load environment variables
# load_dotenv()

# # Initialize Flask app
# app = Flask(__name__)

# #Enable CoRS
# CORS(app)

# # Initialize chatbot
# groq_api_key = os.getenv('GROQ_API_KEY')
# if not groq_api_key:
#     raise ValueError("GROQ_API_KEY is not set. Please check the .env file.")

# chatbot = Chatbot(groq_api_key=groq_api_key)

# # Routes
# @app.route("/")
# def home():
#     return render_template("index.html")

# # Dummy admin credentials
# ADMIN_USERNAME = "admin"
# ADMIN_PASSWORD = "admin"

# @app.route("/api/login", methods=["POST"])
# def login():
#     data = request.json
#     username = data.get("username")
#     password = data.get("password")

#     # Basic login validation
#     if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
#         return jsonify({"success": True, "message": "Login successful!"})
#     else:
#         return jsonify({"success": False, "message": "Invalid username or password."}), 401


# @app.route("/chat", methods=["POST"])
# def chat():
#     user_message = request.json.get("message")
#     if not user_message:
#         return jsonify({"error": "No message provided"}), 400

#     # Get chatbot response
#     bot_response = chatbot.get_response(user_message)
#     return jsonify({"response": bot_response})

# if __name__ == "__main__":
#     app.run(debug=True)





from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from chatbot.chatbot import Chatbot
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


groq_api_key = os.getenv('GROQ_API_KEY')
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set. Please check the .env file.")

chatbot = Chatbot(groq_api_key=groq_api_key)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/chat/new", methods=["POST"])
def create_chat():
    return jsonify({"id": os.urandom(8).hex(), "title": "New Chat"})

@app.route("/api/chat/message", methods=["POST"])
def chat():
    chat_id = request.json.get("chatId") 
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    if not chat_id:
        return jsonify({"error": "No chatId provided"}), 400

    bot_response = chatbot.get_response(user_message)
    return jsonify({"response": bot_response})




# Supported languages
SUPPORTED_LANGUAGES = ["en", "es", "fr", "de", "it", "ja", "zh"]  

@app.route("/api/chat/language", methods=["POST"])
def change_language():
    language = request.json.get("language")
    if not language:
        return jsonify({"error": "No language provided"}), 400

    if language not in SUPPORTED_LANGUAGES:
        return jsonify({"error": f"Language '{language}' is not supported."}), 400

    # Call the new set_language method
    try:
        chatbot.set_language(language)
        return jsonify({"success": True, "language": language})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/api/chat/feedback", methods=["POST"])
def submit_feedback():
    feedback = request.json
    rating = feedback.get("rating")
    comment = feedback.get("comment")

    # Log feedback or process it further
    return jsonify({"success": True, "message": "Feedback received,Thank you for your response "})

if __name__ == "__main__":
    app.run(debug=True)

