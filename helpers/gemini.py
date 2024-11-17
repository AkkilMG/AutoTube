


# import asyncio
from time import sleep
from selenium.webdriver.common.by import By
import requests
import json

async def gemini(text):
    try:
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyBJuk3Nrc3bNPwGoZYdJWlN70RIfdWQWIw"
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
