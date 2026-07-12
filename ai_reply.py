import os
from dotenv import load_dotenv
import google.generativeai as genai

from config import AI_MODEL, REPLY_STYLE

# -----------------------------
# Load Gemini API Key
# -----------------------------
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# -----------------------------
# Gemini Model
# -----------------------------
model = genai.GenerativeModel(AI_MODEL)


def generate_reply(comment):

    prompt = f"""
You are a professional YouTube creator.

Reply Style:
{REPLY_STYLE}

Instructions:

1. Detect the language automatically.
   - Hindi comment → Reply in Hindi.
   - English comment → Reply in English.

2. Reply naturally like a real human.

3. Keep the reply short (1-2 sentences).

4. Never repeat the user's comment.

5. Thank users warmly if they appreciate the video.

6. Answer questions briefly and politely.

7. If the comment gives feedback, acknowledge it respectfully.

8. Use at most ONE emoji, only when it feels natural.

9. Never sound robotic.

10. Do not use hashtags.

11. Return ONLY the reply.

Comment:
{comment}
"""

    try:

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:

        return f"❌ Gemini Error: {e}"