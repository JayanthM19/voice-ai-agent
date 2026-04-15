import requests

def generate_code(prompt):
    full_prompt = f"Write clean Python code for: {prompt}"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": full_prompt,
            "stream": False
        }
    )

    return response.json()["response"]