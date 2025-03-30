import unittest
from chatbot import Chatbot
from memory_manager import MemoryManager

class TestChatbot(unittest.TestCase):
    def test_response_generation(self):
        chatbot = Chatbot()
        response = chatbot.respond("Hello")
        self.assertIsInstance(response, str)

class TestMemoryManager(unittest.TestCase):
    def test_memory_storage(self):
        memory = MemoryManager()
        memory.save_interaction("Hello", "Hi there!")
        context = memory.get_context()
        self.assertIn(("Hello", "Hi there!"), context)

if __name__ == "__main__":
    unittest.main()
