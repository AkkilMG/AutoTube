
import requests
import json
from config import GEMINI_KEY

async def gemini(text):
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_KEY}"
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [{ "parts": [
                {"text": "Can you provide me title (Max of 100 character), description (6-8 sentence with facts from web), tags in certain format for given script.\nformat: { title: "", tags: [], description: '' }"+f"\nscript: {text}"}
            ]}]
        }
        response = requests.post(url, headers=headers, json=data)
        raw = response.json()['candidates'][0]['content']['parts'][0]['text'].replace('```json\n', '').replace('```', '')
        data = json.loads(raw)
        return { 'success': True, 'data': data }
    except Exception as e:
        print(f"Exception occurred (gemini): {e}")
        return { 'success': False }
