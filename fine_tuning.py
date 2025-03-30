import requests

class FineTuner:
    def __init__(self, model_name="phi"):
        self.api_url = "http://localhost:11434/api/fine-tune"
        self.model_name = model_name

    def fine_tune(self, dataset_path):
        with open(dataset_path, "r") as file:
            dataset = file.read()
        payload = {
            "model": self.model_name,
            "dataset": dataset
        }
        response = requests.post(self.api_url, json=payload)
        if response.status_code == 200:
            return "Fine-tuning completed successfully."
        else:
            return f"Error: {response.status_code} - {response.text}"
