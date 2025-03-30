from ollama_integration import OllamaIntegration
from memory_manager import MemoryManager

class Chatbot:
    def __init__(self):
        self.memory = MemoryManager()
        self.ollama = OllamaIntegration()

    def respond(self, prompt):
        context = self.memory.get_context()
        response = self.ollama.generate_response(prompt, context)
        self.memory.save_interaction(prompt, response)
        return response
