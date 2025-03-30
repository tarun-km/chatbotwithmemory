import requests

class OllamaIntegration:
    def __init__(self, model_name="phi"):
        self.api_url = "http://localhost:11434/api/generate"
        self.model_name = model_name

    def generate_response(self, prompt, context=None):
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "context": context
        }
        response = requests.post(self.api_url, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "Error: No response from model.")
        else:
            return f"Error: {response.status_code} - {response.text}"
