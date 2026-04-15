import requests

def classify_intent(text):
    prompt = f"""
    You are an intent classifier.

    Classify into ONLY ONE of:
    - create_file
    - write_code
    - summarize
    - chat

    Return ONLY the label.

    Text: {text}
    """

    response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
)

    if response.status_code != 200:
        return "chat"

    data = response.json()
    print("DEBUG RESPONSE:", data)

    if "response" in data:
        intent = data["response"].strip().lower()
        intent = intent.replace('"', '').replace("'", "")
        print("FINAL INTENT:", intent)
        return intent
    else:
        return "chat"