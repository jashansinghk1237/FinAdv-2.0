# # Zaroori libraries import karein
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import google.generativeai as genai

# # Flask app initialize karein
# app = Flask(__name__)
# # CORS enable karein taaki aapka webpage is server se baat kar sake
# CORS(app)

# # --- GEMINI AI CONFIGURATION ---
# try:
#     # NOTE: Apni API key yahan daalein
#     genai.configure(api_key="AIzaSyCIuGE3mMS8YjKF_MIzIg7k3M-bIm3beyw")
#     model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")
# except Exception as e:
#     print(f"Error configuring Gemini: {e}")
#     model = None

# # --- BABA-JI KA IMPROVED PROMPT ---
# # Maine aapke prompt ko aur behtar bana diya hai
# system_prompt = """
# Aap "Baba-ji" hain, ek anubhavi aur shaant AI sant jo financial mamlon mein salah dete hain.
# Aapka lakshya user ko saral, spasht, aur actionable salah dena hai.

# Niyam:
# 1.  Hamesha "Beta," se shuru karein aur ek aashirvaad ya adhyatmik vichar (spiritual quote) ke saath samapt karein.
# 2.  Jawaab hamesha Hinglish (jaise WhatsApp par likhte hain) mein hona chahiye.
# 3.  Jatil vishayon ko hamesha point-by-point list mein samjhayein.
# 4.  User ke sawaal ko dhyan se samjhein aur seedha usi ka jawab dein.
# ---
# User ka sawaal: 
# """

# # --- API ENDPOINT ---
# # Yeh woh URL hai jise aapka webpage call karega
# @app.route('/ask-babaji', methods=['POST'])
# def ask_babaji():
#     if model is None:
#         return jsonify({"error": "Gemini model is not configured correctly."}), 500

#     user_input = request.json.get('prompt')
#     if not user_input:
#         return jsonify({"error": "Beta, aapne koi sawaal nahi poocha."}), 400

#     try:
#         # User ke input ko humare system prompt ke saath jod dein
#         full_prompt = system_prompt + user_input
        
#         # AI se response generate karwayein
#         response = model.generate_content(full_prompt)
        
#         # Response ko aasan text mein convert karke bhejein
#         return jsonify({"response": response.text})
#     except Exception as e:
#         print(f"Error during generation: {e}")
#         return jsonify({"error": "Beta, abhi kuch takniki samasya aa gayi hai."}), 500

# # Server ko chalane ke liye
# if __name__ == '__main__':
#     app.run(port=5000)






































# Zaroori libraries import karein
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
# Error ko aache se pakadne ke liye
from google.api_core import exceptions as google_exceptions

# Flask app initialize karein
# ... (existing code ... no change) ...
app = Flask(__name__)
CORS(app)

# --- GEMINI AI CONFIGURATION ---
# ... (existing code ... no change) ...
try:
    genai.configure(api_key="AIzaSyCIuGE3mMS8YjKF_MIzIg7k3M-bIm3beyw")
    model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")
except Exception as e:
# ... (existing code ... no change) ...
    model = None

# --- BABA-JI KA IMPROVED PROMPT ---
# ... (existing code ... no change) ...
system_prompt = """
Aap "Baba-ji" hain, ek anubhavi aur shaant AI sant jo financial mamlon mein salah dete hain.
Aapka lakshya user ko saral, spasht, aur actionable salah dena hai.
... (existing code ... no change) ...
User ka sawaal: 
"""

# --- API ENDPOINT ---
@app.route('/ask-babaji', methods=['POST'])
def ask_babaji():
# ... (existing code ... no change) ...
    if model is None:
# ... (existing code ... no change) ...
        return jsonify({"error": "Gemini model is not configured correctly."}), 500

    user_input = request.json.get('prompt')
# ... (existing code ... no change) ...
    if not user_input:
# ... (existing code ... no change) ...
        return jsonify({"error": "Beta, aapne koi sawaal nahi poocha."}), 400

    try:
        # User ke input ko humare system prompt ke saath jod dein
# ... (existing code ... no change) ...
        full_prompt = system_prompt + user_input
        
        # AI se response generate karwayein
# ... (existing code ... no change) ...
        response = model.generate_content(full_prompt)
        
        # Response ko aasan text mein convert karke bhejein
# ... (existing code ... no change) ...
        return jsonify({"response": response.text})

    # --- YEH HAI IMPORTANT CHANGE ---
    except google_exceptions.ResourceExhausted as e:
        # Yeh 429 Quota Error ko aache se pakdega
        print(f"Quota Exceeded Error: {e}")
        return jsonify({"error": "Beta, aaj ka free quota poora ho gaya hai. Kripya thodi der baad (ya kal) fir se koshish karein."}), 429
    except Exception as e:
        # Yeh baaki sabhi errors ko pakdega
        print(f"Error during generation: {e}")
        return jsonify({"error": "Beta, abhi kuch takniki samasya aa gayi hai."}), 500

# Server ko chalane ke liye
# ... (existing code ... no change) ...
if __name__ == '__main__':
    app.run(port=5000)